import awswrangler as wr
import pandas as pd
import logging
import boto3
import os

# Region force against local failure
# boto3.setup_default_session(region_name="us-east-1")

# Configure logging to see outputs in the console/CloudWatch
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Make sure this is your exact bucket name
BUCKET_NAME = os.environ.get("BUCKET_NAME", "ecommerce-lakehouse-javdlg-ar")


def lambda_handler(event, context):
    """
    Main function executed by AWS Lambda.
    event: Contains data about the trigger (e.g., S3 object created).
    context: Contains AWS runtime information.
    """

    # 1. Define logical paths
    input_path = f"s3://{BUCKET_NAME}/raw/orders/olist_orders_dataset.csv"
    output_path = f"s3://{BUCKET_NAME}/clean/orders/"

    try:
        logging.info(f"Step 1: Reading raw data from {input_path}")
        # awswrangler reads directly from S3 into a Pandas DataFrame
        df = wr.s3.read_csv(path=input_path)

        logging.info(f"Step 2: Starting data cleaning. Initial rows: {len(df)}")

        # --- TRANSFORMATIONS (Data Quality) ---
        # A. Drop rows missing crucial information
        df = df.dropna(subset=["order_purchase_timestamp", "customer_id"])

        # B. Cast string to datetime
        df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
        df["order_delivered_customer_date"] = pd.to_datetime(
            df["order_delivered_customer_date"]
        )

        # C. Select only business-relevant columns (noise reduction)
        final_columns = [
            "order_id",
            "customer_id",
            "order_status",
            "order_purchase_timestamp",
            "order_delivered_customer_date",
        ]
        df_clean = df[final_columns]

        logging.info("Step 3: Writing clean data in Parquet format")

        # --- WRITE TO S3 ---
        # awswrangler converts the DF to Parquet and saves it to S3
        wr.s3.to_parquet(
            df=df_clean,
            path=output_path,
            dataset=True,  # Creates a Data Lake style directory structure
            mode="overwrite",  # Overwrites if already exists (for testing purposes)
        )

        logging.info("✅ ETL completed successfully.")
        return {
            "statusCode": 200,
            "body": f"Successfully processed {len(df_clean)} rows.",
        }

    except Exception as e:
        logging.error(f"❌ Error during ETL process: {e}")
        raise e


# Local testing block
if __name__ == "__main__":
    # Simulating an empty event and context for local execution
    lambda_handler({}, None)
