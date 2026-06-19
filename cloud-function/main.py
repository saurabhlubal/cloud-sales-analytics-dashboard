from google.cloud import bigquery


def load_csv_to_bigquery(event, context):

    bucket_name = event["bucket"]
    file_name = event["name"]

    print(f"Processing file: {file_name}")

    client = bigquery.Client()

    table_id = "cloud-data-analytics-dashboard.sales_dataset.sales_table"

    uri = f"gs://{bucket_name}/{file_name}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
        write_disposition="WRITE_APPEND"
    )

    load_job = client.load_table_from_uri(
        uri,
        table_id,
        job_config=job_config
    )

    load_job.result()

    print("CSV loaded successfully")