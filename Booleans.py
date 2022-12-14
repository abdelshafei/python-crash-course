done = True

if done:
    #if done is equal to True, any number other than 0 or a non-empty string
    print('yes')
else:
    #if done is equal to False, 0 or an empty string 
    print('no')    

print(type(done) == bool) #True

done = 'beau'
print(type(done) == bool) #False  
# it will be able to evalute weather this is True or False but the type is not boolean

book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])
print(read_any_book) #True

ingredients_purchased = True
meal_cooked = False

ready_to_serve = all([ingredients_purchased, meal_cooked])
print(ready_to_serve) #False