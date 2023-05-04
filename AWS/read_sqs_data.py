"""
    _summary_
"""
import json
import boto3


def receive_messages_from_sqs(queue_url, message_attributes):
    """
    Receive messages from an SQS queue and process them.

    Parameters:
        queue_url (str): The URL of the SQS queue.
        message_attributes (list): A list of message attributes to retrieve.

    Returns:
        None

    Raises:
        botocore.exceptions.ClientError: An error occurred while communicating with AWS.
    """

    # Create an SQS client
    sqs = boto3.client('sqs')

    # Receive messages from the queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MessageAttributeNames=message_attributes,
        MaxNumberOfMessages=10
    )

    # Process the messages
    for message in response['Messages']:
        body = json.loads(message['Body'])
        print(body)

        # Process the message here using the extracted data

        # Delete the message from the queue after processing
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=message['ReceiptHandle']
        )
