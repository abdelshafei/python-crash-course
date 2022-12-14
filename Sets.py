set1 = {"Roger", "Syd"}
set2 = {"Roger"}

intersect = set1 & set2
print(intersect) #{'Roger'}

mode = set1 | set2
print(mode) #{'Roger', 'Syd'}

inter = set1 - set2
print(inter) #{'Syd'}

mod = set1 > set2
print(mod) #True

mod1 = set1 < set2
print(mod1) #False

print(list(set1)) #['Roger', 'Syd']

#Another thing about sets are that they can not have two of the same item
set3 = {'Roger', "syd", "Roger"}
print(set3) #{'Roger', 'syd'}
