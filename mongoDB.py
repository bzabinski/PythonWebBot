from pymongo import MongoClient


class database:


    def __init__(self):
        self.client = MongoClient()

    def connectToDB(self, dbName):
        self.db = self.client[dbName]
        return self.db

    def addCollection(self, connName):
        self.db.create_collection(connName)

    def connectToCollection(self, connName):
        if not self.db.collection_names().__contains__(connName):
            #Create collection if it doesn't exist
            self.addCollection(connName)
        return collection(self.db[connName])


class collection:

    def __init__(self, col):
        self.col = col
