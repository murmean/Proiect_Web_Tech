from flask import Flask
from mongo_utils import MongoUtils

# app = Flask(__name__)


#
# @app.route('/')
# def hello_world():  # put application's code here
#     return f"{text}"

def main():
    utls = MongoUtils()
    client = utls.connect_to_client()
    utls.show_databases(client)
    database_name = utls.get_database(client, 'users')
    collection = utls.create_collection(database_name, 'users')
    utls.show_collections(database_name)

    print(utls.insert_many_clients(collection))


if __name__ == '__main__':
    main()
    # app.run()
