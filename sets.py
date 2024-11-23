# Creating a set
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
myset = {"apple", "banana", "cherry", "apple"}  # Duplicates are ignored
print("Original Set:", myset)

# Iterating through a set
for item in myset:
    print(item)

# Adding elements
myset.add("orange")
print("After Adding 'orange':", myset)

# Adding multiple elements using update()
tropical = {"pineapple", "mango", "papaya"}
myset.update(tropical)
print("After Update with Tropical Fruits:", myset)

# Removing an item using remove()
myset.remove("banana")  # Raises an error if the item does not exist
print("After Removing 'banana':", myset)

# Removing an item using discard()
myset.discard("cherry")  # Does not raise an error if the item does not exist
print("After Discarding 'cherry':", myset)

# Removing a random item using pop()
removed_item = myset.pop()  # Removes a random item
print("After Pop:", myset, "| Removed Item:", removed_item)

# Clearing all items in the set
myset.clear()
print("After Clearing Set:", myset)

# Deleting the set
del myset
# print(myset)  # This will raise a NameError because myset no longer exists

# Union of sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
union_set = set1.union(set2)
print("Union of Sets:", union_set)

# Intersection of sets
set3 = {"a", "b", "d"}
intersection_set = set1.intersection(set3)
print("Intersection of Sets:", intersection_set)

# Difference of sets
difference_set = set1.difference(set3)
print("Difference of Sets:", difference_set)

# Symmetric difference of sets
symmetric_difference_set = set1.symmetric_difference(set3)
print("Symmetric Difference of Sets:", symmetric_difference_set)

# Checking subset
print("Is set1 a subset of set3?", set1.issubset(set3))

# Checking superset
print("Is set1 a superset of set3?", set1.issuperset(set3))

# Checking disjoint sets
print("Are set1 and set3 disjoint?", set1.isdisjoint(set3))

# Copying a set
copied_set = set3.copy()
print("Copied Set:", copied_set)
