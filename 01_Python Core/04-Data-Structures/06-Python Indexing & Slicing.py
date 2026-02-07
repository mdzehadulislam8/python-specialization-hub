""" ------------> Indexing in Python <------------"""
# What is Indexing in Python?
# Indexing in Python is a way to access individual elements of a sequence (like a string, list, or tuple) using their position. The position of the first element is 0, the second element is 1, and so on. This is known as zero-based indexing.
index = "Python"
print(len(index))  # Output: 6
# In this example, we have a string "Python" which has 6 characters. The index of the first character 'P' is 0, the index of the second character 'y' is 1, and so on until the last character 'n' which has an index of 5.

# Typles of Indexing:
# 1. Positive Indexing: In positive indexing, we start counting from the beginning of the sequence. The first element is at index 0, the second element is at index 1, and so on.
# Example 01:
my_string = "Hello, World!"
print(my_string[0])  # Output: H
print(my_string[7])  # Output: W
# In this example, we access the first character 'H' using index 0 and the eighth character 'W' using index 7.
# Here, 0 -> H, 1 -> e, 2 -> l, 3 -> l, 4 -> o, 5 -> ,, 6 -> space, 7 -> W, 8 -> o, 9 -> r, 10 -> l, 11 -> d, and 12 -> !.
# Example 02:
p1 = "I Love Coding"  # <--- This is a string that we will use to demonstrate positive indexing.
print(p1[0])  # Output: I
print(p1[2])  # Output: L
print(p1[3]) # Output: o
print(p1[4]) # Output: v
print(p1[5]) # Output: e
print(p1[6]) # Output: space
print(p1[7]) # Output: C
print(p1[8]) # Output: o
print(p1[9]) # Output: d
print(p1[10]) # Output: i
print(p1[11]) # Output: n
print(p1[12]) # Output: g
# In this example, we access each character of the string "I Love Coding" using their

# 2. Negative Indexing: In negative indexing, we start counting from the end of the sequence. The last element is at index -1, the second to last element is at index -2, and so on.
# Example 01: 
print(my_string[-1])  # Output: !
print(my_string[-7])  # Output: W
# In this example, we access the last character '!' using index -1 and the eighth character 'W' using index -7.
# Here, -1 -> !, -2 -> d, -3 -> l, -4 -> r, -5 -> o, -6 -> W, -7 -> space, -8 -> , and so on.
# Example 02:
p2 = "I Love Coding" # <-- This is the same string as p1, but we will use negative indexing to access its characters.
print(p2[-1])  # Output: g
print(p2[-2])  # Output: n
print(p2[-3])  # Output: i
print(p2[-4])  # Output: d
print(p2[-5])  # Output: o
print(p2[-6])  # Output: C
print(p2[-7])  # Output: space
print(p2[-8])  # Output: e
print(p2[-9])  # Output: v
print(p2[-10])  # Output: o
print(p2[-11])  # Output: L
print(p2[-12])  # Output: space
print(p2[-13])  # Output: I
# In this example, we access each character of the string "I Love Coding" using negative indexing. The last character 'g' is accessed using index -1, the second to last character 'n' is accessed using index -2, and so on until the first character 'I' which is accessed using index -13.



# Slicing in Python:
# What is Slicing in Python?
# Slicing in Python is a way to access a range of elements from a sequence (like a string, list, or tuple) using a specific syntax. The syntax for slicing is: sequence[start:stop:step]. 
# The start index is inclusive, the stop index is exclusive, and the step determines the increment between indices.

# Why need Slicing in Python?
# Slicing is useful when you want to extract a portion of a sequence without modifying the original sequence. It allows you to create new sequences based on existing ones, which can be helpful for various operations like copying, reversing, or selecting specific elements.
# Positive Slicing: In positive slicing, we use positive indices to specify the start and stop positions of the slice. The start index is inclusive, while the stop index is exclusive.

# Example 01:
my_string = "Hello, World!"
print(my_string[0]+my_string[1]+my_string[2]+my_string[3]+my_string[4])  # Output: Hello
# In this example, we access the first five characters of the string "Hello, World!" using their indices and concatenate them to form the word "Hello". However, this method is not efficient and can be cumbersome for longer sequences.
# So, To avoid this, we do slicing.
print(my_string[0:5])  # Output: Hello
# In this example, we use slicing to access the first five characters of the string "Hello, World!" by specifying the start index (0) and the stop index (5). The result is the same as the previous example, but it is more concise and easier to read.
# Here, 0 is the start index (inclusive) and 5 is the stop index (exclusive), which means we get the characters at indices 0, 1, 2, 3, and 4.
# Here why use 0 and 5? Because we want to access the first five characters of the string, which are at indices 0, 1, 2, 3, and 4. The stop index (5) is exclusive, so it does not include the character at index 5 (which is the comma in this case).

# If I were to take the story from beginning to end:
print(my_string[0:13]) # <-- Will print "Hello, World" from start to finish.
# Most easy way
print(my_string[0:])  # <-- Will print "Hello, World!" starting from index 0 to the end.
print(my_string[3:])  # <-- Will print "lo, World!" starting from index 3 to the end.
print(my_string[:5])  # <-- Will print "Hello" from the beginning to index 5 (exclusive).
print(my_string[:3])  # <-- Will print "Hel" from the beginning to index 3 (exclusive).
print(my_string[:])   # <-- Will print the entire string "Hello, World!".

# If you need "World" from the string:
print(my_string[7:12])  # <-- Will print "World" from index
# If you need "lo, Wo" from the string:
print(my_string[3:8])  # <-- Will print "lo, W" from index 3 to 8 (exclusive).
# If you need "Hello, World!" from the string:
print(my_string[0:13])  # <-- Will print "Hello, World!" from index 0 to 13 (exclusive).

# Another way to do slicing:
print(my_string[0:13:1])  # <-- Will print "Hello, World!" from index 0 to 13 (exclusive) with a step of 1.
# Here, the value of the last 1 from each beginning will be Sum, and my middle point here will not work after 13.
print(my_string[0:13:2])  # <-- Will print "Hlo ol!" from index 0 to 13 (exclusive) with a step of 2.
# Here, the value of the last 2 from each beginning will be Sum, and my middle point here will not work after 13.
print(my_string[0:13:3])  # <-- Will print "Hl r!" from index 0 to 13 (exclusive) with a step of 3.
# Here, the value of the last 3 from each beginning will be Sum, and my middle point here will not work after 13.

# Negative Slicing: In negative slicing, we use negative indices to specify the start and stop positions of the slice. The start index is inclusive, while the stop index is exclusive.
new_string = "Python Programming"
print(new_string[-1:-12]) # <-- Will not print anything because the start index (-1) is greater than the stop index (-12).
# In this example, we are trying to slice the string "Python Programming" using negative indices
# However, since the start index (-1) is greater than the stop index (-12), it does not return any characters. In negative slicing, the start index should be less than the stop index for it to work properly.
print(new_string[-2:-6:-1]) # <-- Will print "gnimmargorP" from index -2 to -6 (exclusive) in reverse order.
# In this example, we slice the string "Python Programming" using negative indices. The start
# index (-2) corresponds to the character 'g' in "Programming", and the stop index (-6) corresponds to the character 'P' in "Programming". Since the stop index is exclusive, it does not include the character at 
# index -6. The step of -1 indicates that we want to slice the string in reverse order, resulting in the output "gnimmargorP".

# Without reverse order
print(new_string[-12:-1]) # <-- Will print "Programming" from index -12 to -1 (exclusive).
# In this example, we slice the string "Python Programming" using negative indices. The start index (-12) corresponds to the character 'P' in "Programming", and the stop index (-1) corresponds to the last character 
# 'g' in "Programming". Since the stop index is exclusive, it does not include the character at index -1, resulting in the output "Programming".



# Let's some problems solve using slicing:

# Problem 01: Take input from the user and print it in reverse order.
# Solution:
user_input = input("Enter a string: ")
reversed_input = user_input[::-1]  # Slicing with a step of -1 to reverse the string.
print(f"Reversed string:{reversed_input}")  # Output: Reversed string: <reversed user input>

# Problem 02: From the user-given input, find the length of the text ‘BD’.
# Solution:
user_input = input("Enter a string: ")
result = user_input.index("BD")  # This will return the index of the first occurrence of 'BD' in the user input.
# If 'BD' is not found in the user input, it will raise a ValueError
print(f"Index of 'BD' is: {result}")  # Output: Index of 'BD' is: <index of 'BD' in user input>


