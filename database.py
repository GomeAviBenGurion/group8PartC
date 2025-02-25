from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://SophieBoca:Boca2025@shopihboca.ib36y.mongodb.net/?retryWrites=true&w=majority&appName=ShopihBoca"

# Create a new client and connect to the server
cluster = MongoClient(uri, server_api=ServerApi('1'))
mydatabase = cluster['SophieBocaDB']
adopters_col = mydatabase['Adopters']
