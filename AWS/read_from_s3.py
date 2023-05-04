"""
_summary_   
"""
import boto3


class S3FileReader:
    """
     _summary_
    """
    def __init__(self, bucket_name, file_key):
        self.bucket_name = bucket_name
        self.file_key = file_key
        self.s3_var = boto3.client('s3')

    def read_file(self):
        """
        read_file _summary_

        :return: _description_
        :rtype: _type_
        """
        obj = self.s3_var.get_object(Bucket=self.bucket_name, Key=self.file_key)
        contents = obj['Body'].read().decode('utf-8')
        return contents

    def write_file(self):
        """
        write_file _summary_
        """
        pass


# Example usage
if __name__ == '__main__':
    reader = S3FileReader('my-bucket', 'my-folder/my-file.txt')
    file_contents = reader.read_file()
    print(file_contents)
