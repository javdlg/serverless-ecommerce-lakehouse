-- We create the logic database in the AWS catalog if not exists, this is the database that we will use in our queries in Athena and in our ETL jobs in AWS Glue.
CREATE DATABASE IF NOT EXISTS ecommerce_db;

-- We create the external table appointing to our Parquet files in S3
CREATE EXTERNAL TABLE IF NOT EXISTS ecommerce_db.orders_clean (
    order_id STRING,
    customer_id STRING,
    order_status STRING,
    order_purchase_timestamp TIMESTAMP,
    order_delivered_customer_date TIMESTAMP
)
STORED AS PARQUET
LOCATION 's3://ecommerce-lakehouse-javdlg-ar/clean/orders/'
tblproperties ("parquet.compress"="SNAPPY");