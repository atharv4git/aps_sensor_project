import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH = "aps_failure_training_set_new.txt"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor_data"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    # converting to JSON
    df.reset_index(drop=True,inplace=True)
    json_records = list(json.loads(df.T.to_json()).values())
    
    # inserting converted records to mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)