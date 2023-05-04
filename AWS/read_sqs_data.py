import boto3
import json

# Create an SQS client
sqs = boto3.client('sqs')

# Set up the queue URL and message attributes
queue_url = 'https://sqs.us-west-2.amazonaws.com/123456789012/my-queue'
message_attributes = ['Attribute1', 'Attribute2', 'Attribute3']

# Receive messages from the queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    MessageAttributeNames=message_attributes,
    MaxNumberOfMessages=10
)

# Process the messages
for message in response['Messages']:
    body = json.loads(message['Body'])
    message_id = message['MessageId']
    attribute1 = message['MessageAttributes']['Attribute1']['StringValue']
    attribute2 = message['MessageAttributes']['Attribute2']['StringValue']
    attribute3 = message['MessageAttributes']['Attribute3']['StringValue']

    # Process the message here using the extracted data

    # Delete the message from the queue after processing
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=message['ReceiptHandle']
    )
