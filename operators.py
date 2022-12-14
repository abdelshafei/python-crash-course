    # Arthmetic operators
1 + 1 #2
2 - 1 #1
2 * 2 #4
4 / 2 #2
4 % 3 #1 ==> this is when you want to find reminder of a long divison of two numbers
4 ** 2 #16 
4 // 2 #2 ==> divides two numbers together and rounds down the answer

# the + operator can also be used for Concatenating Strings, like this:
print("scamp"+" is a good dog")
# arthmetic operators could be used to iterate numbers as well, like this:
age = 8
age += 8 # age = age + 8 

age = 4
age *= 4 # age = age * 4
# and so on...

    # Comparison operators
a = 1
b = 2

a == b #False
a != b #True
a > b # False
a <= b #True 

    # Boolean operators
condition1 = True
condition2 = False

not condition1 #False
condition1 and condition2 #False
condition1 or condition2 #True 

# examples about the 'or' operator 
print(0 or 1) #1
print(False or 'hey') #'hey'
print('hi' or 'hey') #'hi'
print([] or False) #False
print(False or []) #[]

# examples about the 'and' operator
print(0 and 1) #0
print(1 and 0) #0
print(False and 'hey') #False
print('hi' and 'hey') #'hey'
print([] and False) #[]
print(False and []) #False

    # Bitwise operators
'''
& performs binary AND operation
| performs binary OR operation
^ performs binary XOR operation
~ performs a binary NOT operation
<< shift left operation
>> shift right operation
'''
    # is and in operators 
'''
is # the is operator that compares two objects and returns true if both are the same objects
in # this is used to tell if a value is contained in alist or another sequence 
'''
    # Ternary operator
# the slow way of defining a conditional without the ternary operator 
def is_adult(age):
    if age > 18:
        return True
    else:
        return False
# now this is the fast way of defining a conditional wwith a ternary operator 
def is_adult2(age):
    return True if age > 18 else False
