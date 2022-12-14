dog = { "name": "Roger", "age": 85}

print(dog['name']) #Roger

    #replacing elements in a dictionary

dog['name'] =  'syd'
print(dog) #{'name': 'syd', 'age': 85}
print(dog.get('name')) #syd
print(dog.get('color')) #None

print(dog.pop('name')) #syd
print(dog) #{'age': 85}

    # identifying elements from dictionary

print(dog.keys()) #dict_keys(['age'])
print(list(dog.keys())) #['age']

print(dog.values()) #dict_values([85])
print(list(dog.values())) #[85]

print(dog.items()) #dict_items([('age', 85)])

print(len(dog)) #1

dog["favorite food"] = "Meat"
print(dog) #{'age': 85, 'favorite food': 'Meat'} 

del dog['age']
print(dog) #{'favorite food': 'Meat'}

    # copying a dictonary
dogcopy = dog.copy()

