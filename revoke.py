from google.cloud import bigquery
from google.cloud.bigquery.dataset import DatasetReference

def revoke_access():
	
    PROJECT_Id='secops-316111'

    bq = bigquery.Client(project=PROJECT_Id)
    dataset_info = bq.get_dataset("Secops")

    #Specify the entry that will loose access to a dataset
    entry = bigquery.AccessEntry(
        role="roles/bigquery.admin",
        entity_type="userByEmail",
        entity_id="nikhilsingh22222.NS@gmail.com",
    )

    if entry in dataset_info.access_entries:
        entries = list(dataset_info.access_entries)
        entries.remove(entry)
        dataset_info.access_entries = entries
        dataset_info = bq.update_dataset(dataset_info, ["access_entries"])
    else:
        print("Entry wasn't found in dataset_info.access_entries")

    print(dataset_info.access_entries)

if __name__ == '__main__':
    revoke_access()