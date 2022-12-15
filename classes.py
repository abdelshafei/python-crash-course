class Animal:
    def walk(self):
        return 'Walking...'




class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return 'woof!'

roger = Dog("Roger", 8)

print(type(roger)) #<class '__main__.dog'>
print(roger.name) #Roger
print(roger.age) #8
print(roger.bark()) #Woof! 
print(roger.walk()) #Walking...


class count:
    def __init__(self, km):
        self.km = km 

    def convert_to_mile(self):
        return (self.km/2) + (self.km/8)

conversion = count(123)
conversion2 = count(144)
conversion3 = count(20)

print(conversion.convert_to_mile()) #76.875
print(conversion2.convert_to_mile()) #90.0
print(conversion3.convert_to_mile()) #12.5
print(conversion.km) #123
print(conversion2.km) #144
print(conversion3.km) #20

        
