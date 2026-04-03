import json
import boto3

s3 = boto3.client(
    's3',
    region_name='us-east-2',
    endpoint_url='https://s3.us-east-2.amazonaws.com'
)

def lambda_handler(event, context):
    bucket_name = "lab-sebastian-2026-ue-252556588994-us-east-2-an"
    file_name = "archivo.txt"

    url = s3.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': bucket_name,
            'Key': file_name
        },
        ExpiresIn=300
    )

    return {
        'statusCode': 200,
        'body': json.dumps(url)
    }
