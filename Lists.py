    # Understanding Lists

dogs = ['Roger', 1, 'syd', True] 

print('Roger' in dogs) #True
print('Beau' in dogs) #False
print(dogs[0]) #Roger
print(dogs[2]) #syd

# updating items in a list
dogs [2] = 'Beau'
print(dogs) #['Roger', 1, 'Beau', True]
print(dogs[2:4]) #['Beau', True]
print(dogs[:2]) #['Roger', 1]
print(dogs[2:]) #['Beau', True]
print(dogs[-1]) #True
print(dogs[-4]) #Roger
print(len(dogs)) #4
dogs.append('judah')
print(dogs) #['Roger', 1, 'Beau', True, 'judah']  
dogs.extend(['judah', 5])
print(dogs) #['Roger', 1, 'Beau', True, 'judah', 'judah', 5]
dogs += ['judah', 4] # ==> this also provides the same funtionality as the extend() function
print(dogs) #['Roger', 1, 'Beau', True, 'judah', 'judah', 5, 'judah', 4]
dogs.remove('judah')
print(dogs) #['Roger', 1, 'Beau', True, 'judah', 5, 'judah', 4]
print(dogs.pop()) #4
print(dogs) #['Roger', 1, 'Beau', True, 'judah', 5, 'judah']
dogs.insert(2, 'test')
print(dogs) #['Roger', 1, 'test', 'Beau', True, 'judah', 5, 'judah']

# adding multiple items in one index of a list
dogs[1:1] = ['test1', 'test2']
print(dogs) #['Roger', 'test1', 'test2', 1, 'test', 'Beau', True, 'judah', 5, 'judah']  

    # Sorting Lists
# to sort lists you have to have a list containg elements only of one type

items = ['Roger', 'Syd', 'beau', 'Quincy']

items.sort()
print(items) #['Quincy', 'Roger', 'Syd', 'beau']  

# to items beigning with lower case letters then use this, otherwise it will sort the uppercase letters first than the lowercase letters second
items = ['Roger', 'Syd', 'beau', 'Quincy']

items.sort(key=str.lower)
print(items) #['beau', 'Quincy', 'Roger', 'Syd'] 

numbers = [8,4,5,6,4,10,3,2,1,2]

numbers.sort()
print(numbers) #[1, 2, 2, 3, 4, 4, 5, 6, 8, 10]

# to sort the original list without modifying the original list, you must use this
items = ['Roger', 'Syd', 'beau', 'Quincy']

print(sorted(items, key=str.lower)) #['beau', 'Quincy', 'Roger', 'Syd']

print(items) #['Roger', 'Syd', 'beau', 'Quincy']
