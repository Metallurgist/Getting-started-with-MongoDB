# Importing MongoDB
import pymongo

# Password of MongoDB database and using a format to mask the password
password = 'xxxxx'
client = pymongo.MongoClient("mongodb+srv://Burhan:{}@cluster0.pjdknfn.mongodb.net/?retryWrites=true&w=majority".format(password))
db = client.test

database = client['inventory']# Creating a MangoDB Database
collection = database['table']# Creating a Database collection

# Creating a 'data' data and inserting inside 'table' collection
data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]
collection.insert_many(data)

d = collection.find()
for i in d:
    print(i)

print('\n')

# Filtering data's whose status is 'D'
data = collection.find({'status' : 'D'})
for i in data :
    print(i)

print('\n')

# Filtering data's whose status is 'A' | 'P'
data = collection.find({'status' : {'$in':['A','P']}})
for i in data :
    print(i)

print('\n')

# Filtering data's whose status is > D
data = collection.find({'status' : {'$gt':'D'}})
for i in data :
    print(i)

print('\n')

# Filtering data's whose qty is >= 75
data = collection.find({'qty' : {'$gte':75}})
for i in data :
    print(i)

print('\n')

# Filtering data's whose item is 'sketch pad' and qty is >= 95
data = collection.find({'item':'sketch pad','qty':95})
for i in data :
    print(i)

print('\n')

# Filtering data's whose item is 'sketch pad' and qty is >= 75
data = collection.find({'item':'sketch pad','qty':{'$gte':75}})
for i in data :
    print(i)

print('\n')

# Filtering data's whose item is 'sketch pad' or qty is >= 75
data = collection.find({'$or': [{'item': 'sketch pad'}, {'qty': {'$gte': 75}}]})
for i in data :
    print(i)

print('\n')

# Updating a item value 'canvas' with 'burhan'
collection.update_one({'item':'canvas'},{'$set':{'item':'burhan'}})
d = collection.find({'item':'burhan'})
for i in d:
    print(i)

print('\n')

# Deleting a item value 'burhan'
collection.delete_one({'item':'burhan'})
d = collection.find({'item':'burhan'})
for i in d:
    print(i)