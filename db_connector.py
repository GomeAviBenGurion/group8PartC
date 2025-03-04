from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# MongoDB Connection
uri = "mongodb+srv://SophieBoca:Boca2025@shopihboca.ib36y.mongodb.net/?retryWrites=true&w=majority&appName=ShopihBoca"

# Create MongoDB Client
cluster = MongoClient(uri, server_api=ServerApi('1'))
mydatabase = cluster['SophieBocaDB']

# Define collections
adopters_col = mydatabase['Adopters']
requests_col = mydatabase['AdoptionsRequests']
dogs_col = mydatabase['Dogs']
breeds_col = mydatabase['Breeds']

