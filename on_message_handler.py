import json
import boto3
import os

dynamodb = boto3.client('dynamodb')


def handle(event, context):
    message = json.loads(event['body'])['message']

    paginator = dynamodb.get_paginator('scan')

    connection_ids = []

    api_gateway_management_api = boto3.client(
        'apigatewaymanagementapi',
        endpoint_url='https://' + event['requestContext']['domainName'] + '/' + event['requestContext']['stage']
    )

    # Получим все идентификаторы подключений из БД
    for page in paginator.paginate(TableName=os.environ['SOCKET_CONNECTIONS_TABLE_NAME']):
        connection_ids.extend(page['Items'])

    # Отправим полученное сообщение на все подключенные устройства
    for connection_id in connection_ids:
        api_gateway_management_api.post_to_connection(
            Data=message,
            ConnectionId=connection_id['connectionId']['S']
        )

    return {}
