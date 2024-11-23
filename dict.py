# Dictionary is a collection which is ordered** and changeable. No duplicate members.


# Dictionary items are ordered, changeable, and do not allow duplicates.

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name
# 1. Creating a dictionary
thisdict = {
    "brand": "Ford",
    "year": 1964,
    "model": "Mustang"
}

# 2. Access dictionary values and keys
values = thisdict.values()  # Returns all values
keys = thisdict.keys()      # Returns all keys
items = thisdict.items()    # Returns key-value pairs as tuples

print("Values:", values)
print("Keys:", keys)
print("Items:", items)

# 3. Accessing items using a key
print("Brand:", thisdict["brand"])
print("Year:", thisdict.get("year"))

# 4. Updating or adding key-value pairs
thisdict.update({"color": "red"})  # Add or update
thisdict["price"] = 13000          # Direct assignment
print("Updated Dictionary:", thisdict)

# 5. Removing items
thisdict.pop("price")  # Remove specific key
print("After pop:", thisdict)

thisdict.popitem()  # Remove the last inserted key-value pair
print("After popitem:", thisdict)

del thisdict["year"]  # Remove key explicitly
print("After del:", thisdict)

# Clearing all elements
thisdict.clear()
print("After clear:", thisdict)

# Re-creating dictionary
thisdict = {"brand": "Ford", "year": 1964, "model": "Mustang"}

# 6. Copying dictionaries
newdict = thisdict.copy()  # Creates a shallow copy
print("Copied Dictionary:", newdict)

# 7. Nested Dictionaries
myfamily = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011}
}
print("Child1's Name:", myfamily["child1"]["name"])

# 8. Iterating through a dictionary
for key in thisdict:
    print("Key:", key, "Value:", thisdict[key])

for key, value in thisdict.items():
    print(f"{key}: {value}")

# 9. Using the `setdefault` method
thisdict.setdefault("model", "Fiesta")  # Doesn't add if key exists
print("Using setdefault:", thisdict)

# 10. Creating dictionary using `dict` constructor
dict1 = dict(name="John", age=36, country="Norway")
print("Dict Constructor:", dict1)

# 11. Fromkeys method
keys = ("key1", "key2", "key3")
values = 0
newdict = dict.fromkeys(keys, values)
print("Fromkeys:", newdict)

# Full List of Dictionary Methods
"""
1. clear()      - Removes all elements from the dictionary
2. copy()       - Returns a copy of the dictionary
3. fromkeys()   - Creates a new dictionary from a sequence of keys and a value
4. get()        - Returns the value for a specified key
5. items()      - Returns a view object of key-value pairs
6. keys()       - Returns a view object of keys
7. pop()        - Removes the item with the specified key
8. popitem()    - Removes and returns the last inserted key-value pair
9. setdefault() - Returns the value of a key if it exists, or inserts it with a default value
10. update()    - Updates the dictionary with key-value pairs from another dictionary or iterable
11. values()    - Returns a view object of values
12. del         - Deletes a key or the entire dictionary
"""







