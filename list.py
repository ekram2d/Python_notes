# List Operations Example
# ========================

## 1. Basic List Operations
# ----------------------------
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print("\n1. Basic List Operations")
print("Original List:", fruits)
print("First element:", fruits[0])
print("Last element:", fruits[-1])
print("Slice [1:4]:", fruits[1:4])
print("Reversed list (slicing):", fruits[::-1])
print("Length of list:", len(fruits))

## 2. Adding Elements
# --------------------
print("\n2. Adding Elements")
fruits.append('grape')
print("After append:", fruits)
fruits.insert(2, 'mango')
print("After insert at index 2:", fruits)
fruits.extend(['papaya', 'pineapple'])
print("After extend:", fruits)
combined_list = fruits + ['watermelon']
print("After concatenation:", combined_list)

## 3. Removing Elements
# ----------------------
print("\n3. Removing Elements")
fruits.remove('apple')  # Removes the first occurrence
print("After remove 'apple':", fruits)
popped_item = fruits.pop(2)
print("After pop index 2:", fruits, "(Popped item:", popped_item, ")")
fruits.clear()
print("After clear:", fruits)

## 4. Searching and Counting
# ---------------------------
print("\n4. Searching and Counting")
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print("List:", fruits)
print("Is 'pear' in list?:", 'pear' in fruits)
print("Index of 'banana':", fruits.index('banana'))
print("Count of 'apple':", fruits.count('apple'))

## 5. Sorting and Reversing
# -------------------------
print("\n5. Sorting and Reversing")
numbers = [4, 2, 9, 1, 5, 6]
print("Original Numbers:", numbers)
numbers.sort()
print("Sorted list (ascending):", numbers)
numbers.sort(reverse=True)
print("Sorted list (descending):", numbers)
numbers.reverse()
print("Reversed list:", numbers)

## 6. Other Useful Operations
# ----------------------------
print("\n6. Other Useful Operations")
squared = [x**2 for x in numbers]
print("Squares of numbers:", squared)
copied_list = numbers.copy()
print("Copied list:", copied_list)
print("Sum of numbers:", sum(numbers))
print("Min and Max:", min(numbers), max(numbers))

# list to string
joined_string = ",".join(['a', 'b', 'c'])
print("Joined string:", joined_string)

# string to list
split_list = "a ,b, c".split(",")
print("Split list:", split_list)

txt = "welcome to the jungle"
x = txt.split()
print(x)
text=" ".join(x)
print(text)

## 7. Nested Lists
# -----------------
print("\n7. Nested Lists")
nested_list = [[1, 2], [3, 4], [5, 6]]
print("Nested list:", nested_list)
print("Access element [1][0]:", nested_list[1][0])
for sublist in nested_list:
    for item in sublist:
        print("Item:", item)

## 8. Functional Programming with Lists
# --------------------------------------
print("\n8. Functional Programming with Lists")
filtered = list(filter(lambda x: x > 3, numbers))
print("Filtered numbers > 3:", filtered)
mapped = list(map(lambda x: x**3, numbers))
print("Mapped (cubes):", mapped)
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("Product of all numbers:", product)

## 9. Iterating Over a List
# --------------------------
print("\n9. Iterating Over a List")
for item in fruits:
    print("Fruit:", item)
for idx, item in enumerate(fruits):
    print(f"Index {idx}: {item}")

## 10. Advanced Operations
# -------------------------
print("\n10. Advanced Operations")
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print("Zipped list:", zipped)
unzipped = list(zip(*zipped))
print("Unzipped lists:", unzipped)
flat_list = [item for sublist in nested_list for item in sublist]
print("Flattened nested list:", flat_list)
