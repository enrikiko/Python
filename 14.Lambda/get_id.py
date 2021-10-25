import json
import boto3

def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    table = client.Table("my_ip")
    ip = table.get_item(Key={'ip': 'home'})
    return {
            'statusCode': 200,
            'body': json.dumps(ip["Item"]["IP"])
        }
