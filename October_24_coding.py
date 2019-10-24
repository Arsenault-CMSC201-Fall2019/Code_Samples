# Code for Thursday, October 24

#create an empty dictionary
new_dict = {}
print(new_dict)

# Creating a Dictionary
# with Integer Keys
Dict = {1: 'University', 2: 'of', 3: 'Maryland', 4:"Baltimore County"}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

# Creating a Dictionary
# with Mixed keys
new_dict = {'Name': 'Bears', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(new_dict)

# Creating a Dictionary
# with dict() method
new_dict = dict({1: 'Saints', 2: 'For', 3: 'Super Bowl'})
print("\nDictionary with the use of dict(): ")
print(new_dict)

# Creating a Dictionary
# with each item as a Pair
new_dict = dict([(1, 'New'), (2, 'Orleans')])
print("\nDictionary with each item as a pair: ")
print(new_dict)

# Creating an empty Dictionary
new_dict = {}
print("Empty Dictionary: ")
print(new_dict)

# Adding elements one at a time
new_dict[0] = 'Geeks'
new_dict[2] = 'For'
new_dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(new_dict)

# Adding set of values
# to a single Key
new_dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(new_dict)

# Updating existing Key's Value
new_dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(new_dict)

# Adding Nested Key value to Dictionary
new_dict[5] = {'Nested': {'1': 'Life', '2': 'Spartans'}}
print("\nAdding a Nested Key: ")
print(new_dict)

# Python program to demonstrate
# accessing an element from a Dictionary

# Creating a Dictionary
next_dict = {1: 'First', 'name': 'Second', 3: 'Third'}

# accessing a element using key
print("Acessing a element using key:")
print(next_dict['name'])

# accessing a element using key
print("Acessing a element using key:")
print(next_dict[1])

# accessing a element using get()
# method
print("Accessing a element using get:")
print(next_dict.get(3))

# Initial Dictionary
Dict = {5: 'Welcome', 6: 'To', 7: 'UMBC',
        'A': {1: 'Department', 2: 'of', 3: 'CSEE'},
        'B': {1: 'ITE', 2: 'Building'}}
print("Initial Dictionary: ")
print(Dict)

# Deleting a Key value
del Dict[6]
print("\nDeleting a specific key: ")
print(Dict)

# Deleting a Key from
# Nested Dictionary
del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)

# Deleting a Key
# using pop()
Dict.pop(5)
print("\nPopping specific element: ")
print(Dict)

# Deleting an arbitrary Key-value pair
# using popitem()
Dict.popitem()
print("\nPops an arbitrary key-value pair: ")
print(Dict)

# Deleting entire Dictionary
Dict.clear()
print("\nDeleting Entire Dictionary: ")
print(Dict)
