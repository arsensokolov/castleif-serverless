import json
import boto3
import os

dynamodb = boto3.client('dynamodb')


def handle(event, context):
    connection_id = event['requestContext']['connectionId']

    dynamodb.delete_item(
        TableName=os.environ['SOCKET_CONNECTIONS_TABLE_NAME'],
        Key={'connectionId': {'S': connection_id}}
    )

    return {}
