import json
import os
import logging
import boto3
from botocore.exceptions import ClientError

# Configure logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# AWS clients
dynamodb = boto3.resource("dynamodb")
cloudwatch = boto3.client("cloudwatch")

# Environment variable for table
TABLE_NAME = os.environ.get("TABLE_NAME", "ResumeVisitorCounter")
table = dynamodb.Table(TABLE_NAME)


def log_json(level, message, **kwargs):
    log_entry = {
        "level": level,
        "message": message,
        **kwargs
    }
    logger.info(json.dumps(log_entry))


def lambda_handler(event, context):

    # Handle CORS preflight request
    if event.get("httpMethod") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": ""
        }

    try:
        # Update DynamoDB visitor counter
        response = table.update_item(
            Key={"id": "visitor_count"},
            UpdateExpression="ADD #count :inc",
            ExpressionAttributeNames={"#count": "count"},
            ExpressionAttributeValues={":inc": 1},
            ReturnValues="UPDATED_NEW",
        )

        new_count = int(response["Attributes"]["count"])

        # Send custom CloudWatch metric safely
        try:
            cloudwatch.put_metric_data(
                Namespace="ResumeApp",
                MetricData=[
                    {
                        "MetricName": "VisitorCountIncrement",
                        "Value": 1,
                        "Unit": "Count"
                    }
                ]
            )
        except Exception as metric_error:
            log_json(
                "ERROR",
                "Metric submission failed",
                error=str(metric_error),
                request_id=context.aws_request_id
            )

        # Structured logging
        log_json(
            "INFO",
            "Visitor count updated",
            new_count=new_count,
            request_id=context.aws_request_id
        )

        # Successful response
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({"count": new_count})
        }

    except ClientError as e:
        log_json(
            "ERROR",
            "DynamoDB update failed",
            error=str(e),
            request_id=context.aws_request_id
        )

        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({"error": "Error updating visitor count"})
        }