age = 8

print(age.real) #8
print(age.imag) #0
print(age.bit_length()) #4


items = [1, 2, 3, 5]

items.append(3)
print(items) #[1, 2, 3, 5, 3]
print(items.pop())
print(items) #[1, 2, 3, 5]
print(id(items)) #the memory position of the list


