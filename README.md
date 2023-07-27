# SmallAPIProject
Small API project written in Python


Using the given .bz2 file as fixture, create a RESTful API with the following endpoints:
1. /class: Given the name of the MO class, the endpoint should return a sequence of attribute, datatype pairs in JSON format.
2. /attribute: Given the name of the MO attribute, the endpoint should return the datatype, and all parent MO classes.
3. /datatype: Given the name of the datatype, the endpoint should return all MO attributes that belong to this type.
4. /random: This is a generic endpoint that should return a sequence of four response strings from the https://baconipsum.com/json-api/ public API.
