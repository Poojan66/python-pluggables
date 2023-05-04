import boto3


class S3FileReader:
    def __init__(self, bucket_name, file_key):
        self.bucket_name = bucket_name
        self.file_key = file_key
        self.s3 = boto3.client('s3')

    def read_file(self):
        obj = self.s3.get_object(Bucket=self.bucket_name, Key=self.file_key)
        contents = obj['Body'].read().decode('utf-8')
        return contents


# Example usage
if __name__ == '__main__':
    reader = S3FileReader('my-bucket', 'my-folder/my-file.txt')
    file_contents = reader.read_file()
    print(file_contents)
