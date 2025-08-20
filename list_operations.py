# Python program to demonstrate list operations

# Create an empty list
my_list = []

# Append elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("List after appending elements =", my_list)

# Insert value 15 at second position (index 1)
my_list.insert(1, 15)
print("List after inserting 15 at second position:", my_list)

# Extend my_list with another list
my_list.extend([50, 60, 70])
print("List after extending with [50, 60, 70] =", my_list)

# Remove the last element
my_list.pop()
print("List after removing the last element = ", my_list)

# Sort the list in ascending order
my_list.sort()
print("List after sorting in ascending order = ", my_list)

# Find and print the index of value 30
index_of_30 = my_list.index(30)
print("Index of value 30 = ", index_of_30)
