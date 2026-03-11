import os
import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource("dynamodb")
TABLE_NAME = os.environ.get("TABLE_NAME", "ResumeVisitorCounter")
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        response = table.update_item(
            Key={"id": "visitor_count"},
            UpdateExpression="ADD #count :inc",
            ExpressionAttributeNames={"#count": "count"},
            ExpressionAttributeValues={":inc": 1},
            ReturnValues="UPDATED_NEW",
        )

        count = int(response["Attributes"]["count"])

        return {
              "statusCode": 200,
              "headers": {
              "Content-Type": "application/json",
              "Access-Control-Allow-Origin": "*",
               "Access-Control-Allow-Methods": "GET,OPTIONS",
               "Access-Control-Allow-Headers": "Content-Type"
            },
             "body": json.dumps({"count": count})
        }


    except ClientError:
        return {
            "statusCode": 500,
            "body": "Error updating visitor count",
        }
