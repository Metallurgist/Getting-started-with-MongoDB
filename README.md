![hg](https://findlogovector.com/wp-content/uploads/2022/04/mongodb-logo-vector-2022.png)
# Getting started with MongoDB

**PyMongo** is a Python distribution containing tools for working with **[MongoDB](https://www.mongodb.com/)**, and is the recommended way to work with MongoDB from Python. This **[MongoDB Documentation](https://pymongo.readthedocs.io/en/stable/)** attempts to explain everything you need to know to use PyMongo.

**Installing with pip**
```
pip install pymongo
```
**Dependencies**

The correct dependency can be installed automatically along with PyMongo. Support for mongodb+srv:// URIs requires dnspython
```
pip install "pymongo[srv]"
```

* To practise with MongoDB , I have created a free database **Cluster0** with **CLUSTER TIER : M0 Sandbox (General)** with total size of **512.0 MB**
![Cluster0](https://github.com/Metallurgist/Getting-started-with-MongoDB/blob/master/Pics/Cluster0.png)

* Click connect to choose a connection method to connect with your application.
![Cluster0 connect](https://github.com/Metallurgist/Getting-started-with-MongoDB/blob/master/Pics/Cluster0%20connect.png)

* Created Databases and connection as shown here-in below. Click refresh after every data insertion.
![Cluster0 Databases and Collections](https://github.com/Metallurgist/Getting-started-with-MongoDB/blob/master/Pics/Cluster0%20Databases%20and%20Collections.png)

* Lets create a Test Database and Test collections to store our data.
![DataBase](https://github.com/Metallurgist/Getting-started-with-MongoDB/blob/master/Pics/DataBase.png)

Use ```collection.insert_one``` for single entry and ```collection.insert_many``` for pushing multiple data entry into the Collection
