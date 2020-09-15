import os
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\ASHISH\Desktop\GCP\dhamu-gcp-learn.json"


def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name, prefix='tmp', delimiter='/')

    # print(len([1 for blob in blobs]))
    for blob in blobs:
        print(blob.name)


list_blobs('cs-staging')