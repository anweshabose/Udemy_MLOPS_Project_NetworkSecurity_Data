''' This file is made for ensuring successfull connection with Mongodb atlas'''
''' These codes are copied from MongoAtlas '''

# (d:\Udemy\Complete_DSMLDLNLP_Bootcamp\Python\49-End To End MLOPS Project with ETL Pipelines\venv) D:\Udemy\Complete_DSMLDLNLP_Bootcamp\Python\49-End To End MLOPS Project with ETL Pipelines>python Mongo_Atlas.py
#Pinged your deployment. You successfully connected to MongoDB!

#from pymongo.mongo_client import MongoClient

#uri = "mongodb+srv://anweshabose:<password>@cluster0.g0sfswx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

''' Create a new client and connect to the server '''
#client = MongoClient(uri)

''' Send a ping to confirm a successful connection '''
#try:
#    client.admin.command('ping')
#    print("Pinged your deployment. You successfully connected to MongoDB!")
#except Exception as e:
#    print(e)

# (d:\Udemy\Complete_DSMLDLNLP_Bootcamp\Python\49-End To End MLOPS Project with ETL Pipelines\venv) D:\Udemy\Complete_DSMLDLNLP_Bootcamp\Python\49-End To End MLOPS Project with ETL Pipelines>python Mongo_Atlas.py
#Pinged your deployment. You successfully connected to MongoDB!

## ##  ## ##  ## ##  ## ## ## ##  ## ## ## ## ## ------------------------ ## ## ##  ## ##  ## ##  ## ## ## ##  ## ## ##

''' This file is made for pushing the dataset in MongoDB '''
import os
import sys
import json
import pandas as pd
import pymongo
import certifi

from dotenv import load_dotenv
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

''' Load environment variables '''
load_dotenv()

''' Fetch MongoDB URL from environment '''
MongoDB_url = os.getenv("Mongo_connection_url")
if not MongoDB_url:
    raise ValueError("Mongo_connection_url not found in environment variables")

ca = certifi.where()

class NetworkDataExtract:
    def __init__(self):
        try:
            logging.info("Initialized NetworkDataExtract object")
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path: str) -> list:
        """Reads CSV and converts to list of JSON-like dicts."""
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.to_json(orient="records")))
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records: list, database: str, collection: str) -> int:
        """Insert records into the specified MongoDB collection."""
        try:
            mongo_client = pymongo.MongoClient(MongoDB_url, tlsCAFile=ca)
            db = mongo_client[database]
            collection_ref = db[collection]
            result = collection_ref.insert_many(records)
            logging.info(f"Inserted {len(result.inserted_ids)} records")
            return len(result.inserted_ids)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    File_Path = "Network_Data/phisingData.csv"  
    Database = "ANWESHA_1"
    Collection = "NetworkData"

    try:
        network_obj = NetworkDataExtract()
        records = network_obj.csv_to_json_convertor(File_Path)
        logging.info(f"Extracted {len(records)} records from CSV")
        inserted_count = network_obj.insert_data_mongodb(records, Database, Collection)
        logging.info("Data successfully pushed to MongoDB")
        print(f"{inserted_count} records inserted successfully.")
    except Exception as e:
        logging.error(f"Pipeline failed due to: {e}")
        print(f"Error occurred: {e}")



#(d:\Udemy\Complete_DSMLDLNLP_Bootcamp\Python\49-End To End MLOPS Project with ETL Pipelines\venv) D:\Udemy\Complete_DSMLDLNLP_Bootcamp\Python\49-End To End MLOPS Project with ETL Pipelines>python Mongo_Atlas.py
#11055 records inserted successfully.