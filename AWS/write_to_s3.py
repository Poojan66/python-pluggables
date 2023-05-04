import boto3


class S3Writer:
    def __init__(self, bucket_name, key_name):
        self.s3_client = boto3.client('s3')
        self.bucket_name = bucket_name
        self.key_name = key_name

    def write_to_s3(self, data):
        self.s3_client.put_object(
            Bucket=self.bucket_name, Key=self.key_name, Body=data)

# Example usage in AWS Lambda function


def lambda_handler(event, context):
    s3 = S3Writer('my-bucket', 'my-file.txt')
    data = 'Hello, world!'
    s3.write_to_s3(data.encode())
    return {
        'statusCode': 200,
        'body': 'Data written to S3'
    }
