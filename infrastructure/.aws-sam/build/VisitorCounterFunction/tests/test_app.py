import os
import json
import boto3
import pytest
from botocore.stub import Stubber
from boto3.dynamodb.types import TypeDeserializer


# Import the Lambda handler
from backend.visitor_counter import app


class MockTable:
    def update_item(self, **kwargs):
        return {
            "Attributes": {
                "count": {"N": "1"}
            }
        }


def test_lambda_increments_counter_successfully(monkeypatch):
    monkeypatch.setattr(app, "table", MockTable())

    response = app.lambda_handler({}, {})

    assert response["statusCode"] == 200
    assert response["body"] == "1"
