"""
_summary_

"""
from typing import Dict, Any
import boto3


class SQSQueue:
    """
    A class to represent a SQS queue and its methods.
    """

    def __init__(self, queue_url: str) -> None:
        """
        Constructs all the necessary attributes for the SQSQueue object.

        Parameters:
        queue_url (str): The URL of the SQS queue.
        """
        self.queue_url = queue_url
        self.sqs = boto3.client('sqs')

    def push_message(self, message_body: str, user_id: str) -> Dict[str, Any]:
        """
        Pushes a message to the SQS queue for the specified user.

        Parameters:
        message_body (str): The message body to be pushed to the SQS queue.
        user_id (str): The ID of the user to whom the message is intended.

        Returns:
        dict: A dictionary containing the response from SQS.
        """
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

    def recieve_message(self):
        """
        recieve_message _summary_
        """
        pass


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    The lambda function handler which reads message body and user ID from the input event and
    pushes a message to the specified SQS queue.

    Parameters:
    event (dict): The input event that triggered the Lambda function.
    context (AWSLambdaContext): The context object provided by Lambda.

    Returns:
    dict: A dictionary containing the response from SQS.
    """
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
