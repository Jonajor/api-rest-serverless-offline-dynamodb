import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4569")


def get(event, context):
    table = dynamodb.Table('TESTE')

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
