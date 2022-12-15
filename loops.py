    # Understanding Loops

# While Loops    
count = 0
while count < 10:
    print("The condition is True")
    count += 1

print("After the loop")    

# For Loops
items = ['beau', 'syd', 'quincy']
for index, item in enumerate(items):
    print(index, item)

    # Break and Continue  

items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        continue # the program restarts the loop if the item in the list is 2 without printing it
    print(item)

for item in items:
    if item == 2:
        break # the program terminates if the item in the list is 2
    print(item)
    