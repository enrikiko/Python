import json
import boto3

def lambda_handler(event, context):
    ip =  event["requestContext"]["identity"]["sourceIp"]
    client = boto3.resource('dynamodb')
    table = client.Table("my_ip")
    table.put_item(Item={'ip': 'home', 'IP': ip})
    return {
            'statusCode': 200,
            'body': json.dumps(ip)
        }
