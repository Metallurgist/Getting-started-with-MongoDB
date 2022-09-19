# Importing MongoDB
import pymongo

# Password of MongoDB database and using a format to mask the password
password = 'Burhan1994.'
client = pymongo.MongoClient("mongodb+srv://Burhan:{}@cluster0.pjdknfn.mongodb.net/?retryWrites=true&w=majority".format(password))
db = client.test

database = client['myinfo']# Creating a MangoDB Database
collection = database['burhan']# Creating a Database collection
collection1 = database['dpkt']# Creating a Database collection1

# Return all collection record stored inside the Database
for i in collection.find() :
    print(i)