from db_connector import mydatabase  # Import the existing MongoDB connection


def print_collections():
    """ Function to print all collections and their documents """
    print("\n Available Collections in Database:")

    # Get all collections in the database
    collections = mydatabase.list_collection_names()

    if not collections:
        print(" No collections found in the database.")
        return

    # Loop through each collection and print its documents
    for collection_name in collections:
        print(f"\n Collection: {collection_name}")
        collection = mydatabase[collection_name]

        # Retrieve all documents in the collection
        documents = list(collection.find({}))

        if documents:
            for doc in documents:
                print(doc)  # Print each document
        else:
            print("   (Empty Collection)")


# Run the function
if __name__ == "__main__":
    print_collections()
