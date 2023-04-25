import json

jsonString = '''{ "students": [
                    {   "first name" : "John",
                        "last name" : "Smith",
                        "age" : 13.0   },
                    {   "first name" : "Anna",
                        "last name" : "Doe",
                        "age" : 10.0   }
                ]}'''

data_json = json.loads(jsonString)

print(data_json)

print(data_json['students'])

print(data_json['students'][1])

data_of_class = {"teacher": {"first name":"Marry", "last name":"Brown"},
                 "students" : [
                     {"first name":"John", "last name":"Smith", "age":13},
                     {"first name":"Anna", "last name":"Doe","age":10.0}
                     ]
                 }

json_of_class = json.dumps(data_of_class)
print(json_of_class)
