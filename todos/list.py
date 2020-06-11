import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4569")


def list(event, context):
    table = dynamodb.Table('TESTE')

    # fetch all todos from the database
    result = table.scan()

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }

    return response
