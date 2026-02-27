import boto3
import os
from botocore.exceptions import ClientError

# 1. Variable configurations
# We use the exactly name of the bucket recently created in AWS S3
BUCKET_NAME = "ecommerce-lakehouse-javdlg-ar"
# Local path where the CSV files are stored
LOCAL_FILE_PATH = "../../data/olist_orders_dataset.csv"
# Logic path in S3 where the files will be stored (simulating a partition per data domain)
S3_KEY_NAME = "raw/orders/olist_orders_dataset.csv"


def upload_to_s3(local_file, bucket, s3_key):
    """
    Uploads a file to an S3 bucket.
    """
    # Initialize the S3 client
    s3_client = boto3.client("s3")

    print(f"Uploading {local_file} to s3://{bucket}/{s3_key}...")

    try:
        # Upload the file to S3
        s3_client.upload_file(local_file, bucket, s3_key)
        print("Upload successful!")
    except FileNotFoundError:
        print(f"Error: The file {local_file} was not found.")
    except ClientError as e:
        print(f"Error uploading file: {e}")


if __name__ == "__main__":
    # Check if the local file exists before attempting to upload
    if os.path.exists(LOCAL_FILE_PATH):
        upload_to_s3(LOCAL_FILE_PATH, BUCKET_NAME, S3_KEY_NAME)
    else:
        print(f"Error: The local file {LOCAL_FILE_PATH} does not exist.")
