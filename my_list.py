# create an empty list
My_list = []

# Append elements to the list 10, 20, 30, 40.
My_list.append(10)
My_list.append(20)
My_list.append(30)
My_list.append(40)

# Insert 15 at the second position (index1)
My_list.insert(1, 15)

# Extend My_list with another list 
My_list.extend([50, 60, 70])

# Remove the last element
My_list.pop()

# Sort the list in ascending order
My_list.sort()

# Find and print the index value of 30
index_30 = My_list.index(30)
print("index of 3o:", index_30)

# Print the final list
print("Final list:", My_list)