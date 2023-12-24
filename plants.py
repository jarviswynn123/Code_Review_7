from google.cloud import bigquery

client = bigquery.Client()

print("successfully created a BigQuery client")
print(f"Project: {client.project}")

for dataset in client.list_datasets():
    dataset_id = dataset.dataset_id
    print(f"dataset id: {dataset_id}")


dataset_ref = client.get_dataset("plants")
tables = client.list_tables("plants")

for table in tables:
    print(f"table name: {table.table_id}")