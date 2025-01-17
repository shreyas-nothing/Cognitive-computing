#5. Write a program to rename a key city to location in the following dictionary: 
# data = {"city": "New York", "population": 8419600, "area": 468.9} .

data = {"city": "New York",
        "population": 8419600,
        "area": 468.9}

data["location"]=data.pop("city")
print(data)