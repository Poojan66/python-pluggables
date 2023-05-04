"""
Module: s3_writer

This module provides a class to write data to an S3 bucket.

"""

import boto3


class S3Writer:
    """
    A class to write data to an S3 bucket.

    Attributes:
    - bucket_name (str): The name of the S3 bucket.
    - key_name (str): The name of the key or object in the bucket.
    """

    def __init__(self, bucket_name, key_name):
        self.s3_client = boto3.client('s3')
        self.bucket_name = bucket_name
        self.key_name = key_name

    def write_to_s3(self, data):
        """
        Write data to S3 bucket.

        Args:
        - data (bytes): The data to be written to the S3 bucket.

        Returns:
        None
        """
        self.s3_client.put_object(
            Bucket=self.bucket_name, Key=self.key_name, Body=data)

    def read_from_s3(self):
        """
        read_from_s3 _summary_

        :return: _description_
        :rtype: _type_
        """
        pass

# Example usage in AWS Lambda function


def lambda_handler(event, context):
    """
    AWS Lambda function to write data to an S3 bucket.

    Args:
    - event (dict): A dictionary containing the event data.
    - context (object): An object containing the runtime information.

    Returns:
    A dictionary containing the status code and a message indicating the
    status of the operation.
    """
    s3_var = S3Writer('my-bucket', 'my-file.txt')
    data = 'Hello, world!' + event
    s3_var.write_to_s3(data.encode())
    return {
        'statusCode': 200,
        'body': 'Data written to S3'
    }
