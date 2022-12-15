    # Understanding Functions
def HELLO(name = "my friend", age = 18):
    print(f"Hello there {name}! I have heard that you are {age} years old?")
HELLO("Abdo", 21) #Hello there Abdo! I have heard that you are 21 years old?
HELLO("Quincy", 119) #Hello there Quincy! I have heard that you are 119 years old?
HELLO() #Hello there my friend! I have heard that you are 18 years old?

def change(value):
    value["name"] = "syd"

    return value
    
val = {"name": "beau"}
print(change(val)) #{'name': 'syd'}    

    # Variable scope
# Global variable    
age = 8

def test():
    print(age)

print(age) #8
test() #8    

# Local variable

def test():
    age = 18
    print(age)

#print(age) ==> it will output an error since the variable has only been declared inside the function scope which would make it a local variable and not a global variable since it had not been declared outside the function scope
test() #8

    # Nested Functions 

def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)

talk('I am going to buy the milk')  

def count():
    count = 0

    def increment():
        nonlocal count
        count += 1
        print(count)

    increment()

count()    

    # Closures

def  counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment

increment = counter() 

print(increment()) #1
print(increment()) #2
print(increment()) #3
  