Sure, here's an example of building an ETL pipeline using Python and Azure services:

1. First, you'll need to set up an Azure storage account where you can store your data. You can do this by logging into the Azure portal and creating a new storage account.

2. Once your storage account is set up, you can use the Azure Blob Storage API to connect to it and access your data. Install the `azure-storage-blob` package using pip:

```
pip install azure-storage-blob
```

3. Next, you'll need to write Python code to extract your data from its source and load it into Azure Blob Storage. Here's an example:

```python
import pandas as pd
from azure.storage.blob import BlobServiceClient

# read data from source (in this example, a CSV file)
data = pd.read_csv('source_file.csv')

# create a connection to your Azure storage account
connection_string = '<your-connection-string>'
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# create a new blob container to store your data
container_client = blob_service_client.get_container_client('<container-name>')
container_client.create_container()

# save the data to a new blob in your container
blob_client = container_client.get_blob_client('<blob-name>')
blob_client.upload_blob(data.to_csv(index=False), overwrite=True)
```

4. Once your data is in Azure Blob Storage, you can use Azure Data Factory to transform it into the desired format and load it into your destination database. Here's an example of a Data Factory pipeline that reads data from a CSV file in Blob Storage, transforms it using a Databricks notebook, and writes the output to an Azure SQL database:

```
{
    "name": "myPipeline",
    "properties": {
        "activities": [
            {
                "name": "inputBlob",
                "type": "BlobSource",
                "linkedServiceName": "myStorageAccount",
                "typeProperties": {
                    "recursive": false,
                    "folderPath": "inputFolder",
                    "fileName": "inputFile.csv"
                }
            },
            {
                "name": "databricksNotebook",
                "type": "DatabricksNotebook",
                "dependsOn": [
                    {
                        "activity": "inputBlob",
                        "dependencyConditions": [
                            "Succeeded"
                        ]
                    }
                ],
                "policy": {
                    "timeout": "7.00:00:00",
                    "retry": 0,
                    "retryIntervalInSeconds": 30,
                    "secureOutput": false
                },
                "typeProperties": {
                    "notebookPath": "/myNotebook",
                    "baseParameters": {
                        "inputFilePath": {
                            "value": "@activity('inputBlob').output.first().filePath"
                        }
                    },
                    "sparkJobLinkedService": {
                        "referenceName": "myDatabricksLinkedService",
                        "type": "LinkedServiceReference"
                    },
                    "notebookLanguage": "PYTHON"
                }
            },
            {
                "name": "outputSql",
                "type": "AzureSqlTable",
                "dependsOn": [
                    {
                        "activity": "databricksNotebook",
                        "dependencyConditions": [
                            "Succeeded"
                        ]
                    }
                ],
                "policy": {
                    "timeout": "7.00:00:00",
                    "retry": 0,
                    "retryIntervalInSeconds": 30,
                    "secureOutput": false
                },
                "typeProperties": {
                    "tableName": "outputTable",
                    "schemaName": "dbo",
                    "writeBatchSize": 10000,
                    "sqlWriterStoredProcedureName": "sp_table