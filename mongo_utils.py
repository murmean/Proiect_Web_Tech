from pymongo import MongoClient
import re


class MongoUtils:
    """
    Utility class to manage MongoDB operations
    """
    @staticmethod
    def connect_to_client():

        connection_string = "mongodb://127.0.0.1:27017/mongosh?directConnection=true&serverSelectionTimeoutMS=2000"

        try:
            client = MongoClient(connection_string)
            return client
        except Exception as e:
            print(f"Couldn't connect to MongoDB database got: {e} instead")

    @staticmethod
    def get_database(client: MongoClient, database_name: str):

        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        try:

            return client[database_name]
        except Exception as e:
            print(f"Couldn't connect to MongoDB database got: {e} instead")

    @staticmethod
    def create_collection(database_name, collection_name: str):
        """Create a new mongodb collection
        :param database_name: name of the database
        :param collection_name: name of the collection
        """
        collection_name = database_name[collection_name]
        return collection_name

    @staticmethod
    def show_collections(database_name):
        """Prints all available collections on the given MongoDB database.
        :param database_name: name of the database
        """
        print(database_name.list_collection_names())

    @staticmethod
    def show_databases(client: MongoClient):
        """Prints all available databases
        :param client: MongoDB client
        """
        print(client.list_database_names())

    @staticmethod
    def insert_one_client(collection_name):
        """Inserts a new client into the MongoDB database.
        :param collection_name: Name of the collection to insert into
        """
        # TODO very if input is only characters
        name = input("Enter name of client")
        age = input("Enter age of client")
        job = input("Enter client's job")

        item_1 = {
            "name": name,
            "age": age,
            "job": job
        }
        collection_name.insert_one(item_1)

    @staticmethod
    def insert_many_clients(collection_name):
        # TODO verify input

        client_list = []
        client_num = input("How many clients do you want to add?")
        for i in range(1, int(client_num) + 1):
            name = input(f"Enter name of client {i}")
            age = input(f"Enter age of client {i}")
            job = input(f"Enter client's {i} job")
            client_list.append({"name": name, "age": age, "job": job})
        collection_name.insert_many(client_list)

        return client_list
