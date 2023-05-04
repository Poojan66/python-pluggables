Here's an example of creating an ETL pipeline using Docker, Python, Pandas, and AWS:

1. Start by creating a Dockerfile that sets up the necessary environment for your ETL pipeline, including Python, Pandas, and any other required packages.

```
FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "etl_pipeline.py"]
```

2. Create a `docker-compose.yml` file to define the services that will be used in your pipeline.

```
version: '3'
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - .:/app
    environment:
      AWS_ACCESS_KEY_ID: ${AWS_ACCESS_KEY_ID}
      AWS_SECRET_ACCESS_KEY: ${AWS_SECRET_ACCESS_KEY}
      AWS_DEFAULT_REGION: ${AWS_DEFAULT_REGION}
    depends_on:
      - db
  db:
    image: postgres:12-alpine
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
```

3. Create a Python script `etl_pipeline.py` that will perform the ETL operations. Here's an example of how this might look:

```python
import pandas as pd
import psycopg2
import boto3

# Load data from source
df = pd.read_csv('source_data.csv')

# Transform data
df['new_column'] = df['old_column'].apply(lambda x: x * 2)

# Load data to target
conn = psycopg2.connect(
    host="db",
    port=5432,
    database="mydatabase",
    user="myusername",
    password="mypassword"
)
cursor = conn.cursor()
for index, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO mytable (col1, col2)
        VALUES (%s, %s)
        """,
        (row['new_column'], row['other_column'])
    )
conn.commit()

# Upload processed data to AWS S3
s3 = boto3.client('s3')
with open('processed_data.csv', 'rb') as f:
    s3.upload_fileobj(f, 'my-bucket', 'processed_data.csv')
```

4. Start the Docker containers using `docker-compose up`. This will start the Python script in the `app` container, which will read data from the `source_data.csv` file, transform it, and load it into a PostgreSQL database running in the `db` container. The script will also upload the processed data to an AWS S3 bucket.

By following these steps, you can create a simple ETL pipeline using Docker, Python, Pandas, and AWS. Of course, this is just a starting point, and you may need to modify the pipeline to suit your specific needs.