from google.cloud import bigquery

client = bigquery.Client()

for dataset in client.list_datasets():
    dataset_id = dataset.dataset_id

dataset_ref = client.get_dataset("plants")

tables = client.list_tables("plants")

for table in tables:
    print(f"table name: {table.table_id}")