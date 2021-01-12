motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# modifying values of a list values
motorcycles[0] = 'ducati' # updates the first value from honda to ducati
print(motorcycles)

# adding elements to a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati') # adds the new item to the end of the list
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# inserting elements into a list
motorcycles.insert(1, 'ducati') # inserts item to second position
print(motorcycles)

# deleting elements from a list
del motorcycles[1] # deletes item at second position
print(motorcycles)

# popping last items from a list so they can be reusable
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print("The last motorcycle I owned was a " + popped_motorcycle.title() + ".")

# popping items from any position in a list so they can be reusable
motorcycles = ['honda', 'yamaha', 'suzuki']
second_owned = motorcycles.pop(1) # pops second item
print("The second motorcycle I owned was a " + second_owned.title() + ".")

# removing the first occurence of an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
expensive_moto = 'ducati'
motorcycles.remove(expensive_moto) # removes item matchin suzuki string
print(motorcycles)
print("A " + expensive_moto.title() + " is too expensive for me!")