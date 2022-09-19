# Importing MongoDB
import pymongo

# Password of MongoDB database and using a format to mask the password
password = 'xxxxx'
client = pymongo.MongoClient("mongodb+srv://Burhan:{}@cluster0.pjdknfn.mongodb.net/?retryWrites=true&w=majority".format(password))
db = client.test

database = client['myinfo']# Creating a MangoDB Database
collection = database['burhan']# Creating a Database collection
collection1 = database['dpkt']# Creating a Database collection1

print('\n')

# Return all collection record stored inside the Database
record = collection.find()
for i in record :
    print(i)

print('\n')

# Find one particular record out from the entire databases where company name filter
data = collection.find({'companyName' : 'iNeuron'})
for i in data :
    print(i)

print('\n')

# Find one particular record out from the entire database that starts (%gt) with 'S'
data = collection.find({'courseOffered' : {'$gt':'s'}})
for i in data :
    print(i)

# Find one particular record out from the entire database that starts (%gt) with 'S'
data = collection.find({'product' : {'$gt':'Master Program'}})
for i in data :
    print(i)