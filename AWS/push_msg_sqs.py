import boto3


class SQSQueue:
    def __init__(self, queue_url):
        self.queue_url = queue_url
        self.sqs = boto3.client('sqs')

    def push_message(self, message_body, user_id):
        message_attributes = {
            'UserId': {
                'DataType': 'String',
                'StringValue': user_id
            }
        }

        response = self.sqs.send_message(
            QueueUrl=self.queue_url,
            MessageBody=message_body,
            MessageAttributes=message_attributes
        )

        return response


def lambda_handler(event, context):
    # Read message body and user ID from event
    message_body = event['message_body']
    user_id = event['user_id']

    # Instantiate SQSQueue class with SQS queue URL
    queue_url = 'https://sqs.<aws-region>.amazonaws.com/<account-id>/queue-name'
    queue = SQSQueue(queue_url)

    # Push message to SQS queue for the specified user
    response = queue.push_message(message_body, user_id)

    # Return response from SQS
    return response
