from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username, password):
        # MongoDB Connection Variables
        self.USER = username
        self.PASS = password
        self.HOST = 'nv-desktop-services.apporto.com'
        self.PORT = 32081
        self.DB = 'AAC'
        self.COL = 'animals'
        
        # Initialize MongoDB Connection
        self.client = MongoClient(f'mongodb://{self.USER}:{self.PASS}@{self.HOST}:{self.PORT}')
        self.database = self.client[self.DB]
        self.collection = self.database[self.COL]

    def create(self, data):
        """Inserts a document into the collection. Returns True if successful, False otherwise."""
        if data is not None:
            try:
                self.collection.insert_one(data)  # data should be a dictionary
                return True
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
        else:
            raise ValueError("Nothing to save, because data parameter is empty")

    def read(self, criteria=None):
        """Queries documents based on criteria. Returns a list of documents if successful, empty list otherwise."""
        try:
            criteria = criteria or {}
            result = list(self.collection.find(criteria))
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def update(self, criteria, update_data):
        """Updates documents based on criteria. Returns the number of documents modified."""
        try:
            update_result = self.collection.update_many(criteria, {'$set': update_data})
            return update_result.modified_count
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0

    def delete(self, criteria):
        """Deletes documents based on criteria. Returns the number of documents removed."""
        try:
            delete_result = self.collection.delete_many(criteria)
            return delete_result.deleted_count
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0


