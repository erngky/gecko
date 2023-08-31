from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
import os

project_id = "YOUR_PROJECT_ID"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"YOUR_CREDENTIALS.json"

client = bigquery.Client()
table_id = "DESTINATION_TABLE_ID"
file_path = r"twitter_handles.csv"

job_config = bigquery.LoadJobConfig(
    source_format = bigquery.SourceFormat.CSV , skip_leading_rows = 1, autodetect=True,
        write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
)

with open(file_path, "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config = job_config)

table = client.get_table(table_id)

