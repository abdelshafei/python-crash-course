names = ('Roger', 'Syd')

print(names[0]) #Roger
print(names.index('Roger')) #0

print(len(names)) #2
print(names[-1]) #Syd

print('Roger' in names) #True
print('Beau' in names) #False

print(names[0:2]) #('Roger', 'Syd')

names = ('Roger', 'Syd', 'Beau')
print(sorted(names)) #['Beau', 'Roger', 'Syd']

newtuple = names + ('Tina', 'Quincy')
print(newtuple) #('Roger', 'Syd', 'Beau', 'Tina', 'Quincy')