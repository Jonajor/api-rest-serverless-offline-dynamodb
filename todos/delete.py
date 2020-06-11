
import boto3
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4569")


def delete(event, context):
    table = dynamodb.Table('TESTE')

    # delete the todo from the database
    table.delete_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response
    response = {
        "statusCode": 200
    }

    return response
