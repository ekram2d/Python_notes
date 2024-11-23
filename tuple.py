# Creating a tuple
mytuple = ("apple", "banana", "cherry", "cherry")
print("Original Tuple:", mytuple)

# Accessing elements
print("Element at index 3:", mytuple[3])  # Access specific element
print("Slice of tuple:", mytuple[:])     # Slice the tuple

# Iterating through a tuple
print("Iterating through tuple:")
for item in mytuple:
    print(item)

# Tuples are immutable, but you can update indirectly by converting to a list and back to a tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"  # Modifying the list
x = tuple(y)   # Converting back to tuple
print("Updated Tuple:", x)

# Adding elements to a tuple (create a new tuple and concatenate)
thistuple = ("apple", "banana", "cherry")
new_tuple = ("orange",)  # Note the comma; without it, it’s not a tuple
thistuple += new_tuple
print("Tuple after addition:", thistuple)

# Tuple unpacking
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits  # Unpack into variables
print("Unpacked:", green, yellow, red)

# Counting occurrences of an element
print("Count of 'cherry':", mytuple.count("cherry"))

# Finding the index of an element
print("Index of 'banana':", mytuple.index("banana"))

# Nested tuples
nested_tuple = (1, 2, ("inner1", "inner2"), 4)
print("Nested Tuple:", nested_tuple)
print("Accessing Nested Element:", nested_tuple[2][1])  # Access inner tuple

# Tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print("Combined Tuple:", combined_tuple)

# Tuple repetition
repeated_tuple = ("A",) * 3
print("Repeated Tuple:", repeated_tuple)

# Checking for membership
print("Is 'apple' in mytuple?", "apple" in mytuple)

# Length of a tuple
print("Length of mytuple:", len(mytuple))

# Minimum and Maximum
numbers = (10, 20, 5, 40, 15)
print("Minimum value:", min(numbers))
print("Maximum value:", max(numbers))

# Converting a list to a tuple
sample_list = [1, 2, 3]
converted_tuple = tuple(sample_list)
print("Converted from List to Tuple:", converted_tuple)

# Sorting a tuple (returns a list)
unsorted_tuple = (3, 1, 4, 2)
sorted_list = sorted(unsorted_tuple)
print("Sorted Tuple as List:", sorted_list)

# Deleting a tuple
del_tuple = ("temp", "delete me")
print("Before deletion:", del_tuple)
del del_tuple
# print(del_tuple)
# print(del_tuple)  # This would raise a NameError because it’s deleted

# Tuple Methods Overview
"""
1. count(item)    - Returns the number of times a value appears in the tuple.
2. index(item)    - Returns the index of the first occurrence of the value.
"""

# Summary of Tuple Characteristics:
"""
1. Ordered: Items have a defined order.
2. Immutable: Cannot be changed after creation.
3. Duplicates Allowed: Tuples can have duplicate values.
4. Can store mixed data types.
"""
