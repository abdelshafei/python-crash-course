# strings could be identified by like this: 
"beau"
"""beau"""
'beau'
# strings can be assigned to variables
name = 'beau'
# strings can be concatenated like this:
concatenated_phrases = "beau"+" is my name" #"beau is my name"
concatenated_phrases = name + " is my name" #"beau is my name"
name += " is my name" #"beau is my name"
    # defining a multiline string with a special syntax
print("""Beau is

39

years old
""") 

    # Using string methods
print('beau'.upper()) #BEAU
print('bEAu'.lower()) #beau
print('beau person'.title()) #Beau Person
print(len('beau')) #4
print('au' in 'beau') #True

    #Escaping Characters
name = "Be\"'au"
print(name) #Be"'au
name = 'be"au'
print(name) #be"au
# creating a new line as an escaping character
name = "be\nau"
print(name)#be
           #au
name = 'be\\au'
print(name) #be\au

    #String Characters & Slicing
name = 'Beau'

print(name[1]) #e
print(name[0]) #B
print(name[-1]) #u
print(name[1:2]) #e
print(name[1:3]) #ea
print(name[0:5]) #Beau
print(name[:5]) #Beau
print(name[2:]) #au