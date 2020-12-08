import boto3
import os

dynamodb = boto3.client('dynamodb')


def handle(event, context):
    connection_id = event['requestContext']['connectionId']

    # Добавим connectionId подключенного устройства в БД
    dynamodb.put_item(
        TableName=os.environ['SOCKET_CONNECTIONS_TABLE_NAME'],
        Item={
            'connectionId': {
                'S': connection_id
            }
        }
    )

    return {}
