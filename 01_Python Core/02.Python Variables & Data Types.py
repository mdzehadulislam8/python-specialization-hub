
"""
              <------------------ Variable ----------------------->
In programming, a Variable is like a labeled bottle that holds data. It allows you to store, retrieve, and manipulate information in your code.

"""

# A Variable is the bottle (container), and Data is the water (content). The variable provides a named space, while the data is the
# actual value kept inside. You can change the data (refill the bottle) whenever needed while keeping the same variable name.


# Variable is a container to store data values.
# In Python, you don't need to declare the type of variable explicitly.
# The type is inferred from the value assigned.

# 1. First create a variable name must start with a letter or underscore (_), followed by letters, digits, or underscores.
# Variable names are case-sensitive.

# The correct way to use variables is:
a =  20 # a is a variable and 20 is data assigned to it.
my_variable = 10
_store123 = "Hello, World!"

# 2. Variable names are case sensitive (age, Age and AGE are three different variables)
age = 25
             # <----------- Different Variable beacause two different cases one is small(age) and other is capital(Age)
Age = 30 


# The error will occur if you use the variable as follows: 
# A Variable name cannot start with a number ----> like : 112store  
# 1st_variable = 10  # <-- This will raise a SyntaxError
# A Variable name cannot contain special characters like @, $, %, etc.
# my@var = 15       # <-- This will raise a SyntaxError
# A Variable name cannot be a reserved keyword in Python
# for = 20         # <-- This will raise a SyntaxError


# Where the data is being stored:
a = 10
print (id(a))  # Output: 140722769095384; prints the memory address of the variable a
# Every time you assign a value to a variable, Python creates an object in memory to hold that value and the variable name points to that object.


"""
  <------------------- Data Types in Python --------------------> 
Data Types define what kind of "liquid" or content you are storing in your variable "bottle." For example, 
an Integer represents whole amounts like 500 (ml), while a Float handles decimal values like 1.5 (liters). If
 you want to store a label or name, you use a String, which is text wrapped in quotes like "Pure Water", and for simple
   yes/no states, you use a Boolean to check if the bottle is full (True) or empty (False).

"""

# Data Types ----> Numbers, Strings, Lists, Dictionaries, Tuples, Sets, Booleans, Range, etc.
# Numbers: Every numeric value in Python is an object of the 'number' data type.
# Strings: A sequence of characters enclosed in single or double quotes.
# Booleans: Represents one of two values: True or False.

# Basic Data Types:
# Lists: An ordered collection of items which can be of different data types.
# Dictionaries: A collection of key-value pairs.
# Tuples: An ordered, immutable collection of items.
# Sets: An unordered collection of unique items.
# Range: Represents an immutable sequence of numbers.

"""
  <------------------- Number Data Type -------------------->
Numbers are one of the most commonly used data types in programming. They are used to represent numeric values and perform mathematical operations."""

# Number Data Type:
# 1=> 0, 1, 2, 10000, 63463, ... (Integers)
# 2=> 1.1, 2.5, 40.70, ... (Floating Point Numbers)
# 3=> Complex Numbers -> 1+2j, 5+3j, .... (used in advanced mathematics)

# Example of Number:
num1 = 1032467234  # Integer
num2 = 3.14        # Float
num3 = 2 + 3j      # Complex Number always has 'j' or 'J' to represent the imaginary part don't use 'i' like in mathematics
print(type(num1))  # Output: <class 'int'>
print(type(num2))  # Output: <class 'float'>    
print(type(num3))  # Output: <class 'complex'>
print(num1) # Output: 1032467234
print(num2) # Output: 3.14
print(num3) # Output: (2+3j)


"""
  <------------------- String Data Type --------------------> 
  Strings are sequences of characters used to represent text. They can include letters, numbers, symbols, and spaces. In Python, strings are enclosed in either single quotes (' ') or double quotes (" ")."""

# Example of String:
str1 = 'Hello, World!'        # Using single quotes
str2 = "Python is awesome."    # Using double quotes

# Note : In Python, anything written inside quotes (' ' or " ") is always treated as a string—whether it is a character, a word, or even a number.
# example : 
str3 = '12345'  # This is a string, not a number
print(type(str3))  # Output: <class 'str'>
str4 = "4.2"     # This is also a string
print(type(str4))  # Output: <class 'str'>
str5 = 'True'    # This is a string, not a boolean
print(type(str5))  # Output: <class 'str'>
str6 = "I am 24 years old" # This is a string with numbers and text
print(type(str6))  # Output: <class 'str'>


# Now, if I want to get the output of all the strings, then:
print(str1)  # Output: Hello, World!
print(str2)  # Output: Python is awesome. 
print(str3)  # Output: 12345
print(str4)  # Output: 4.2
print(str5)  # Output: True
print(str6)  # Output: I am 24 years old




"""  <------------------- Boolean Data Type -------------------->
Booleans are a data type that can hold one of two values: True or False.
 They are commonly used in programming for decision-making and controlling the flow of a program based on conditions."""

# Example of Boolean:
bool1 = True # Always True with a capital 'T'
bool2 = False # Always False with a capital 'F'
print(type(bool1))  # Output: <class 'bool'>
print(type(bool2))  # Output: <class 'bool'>
print(bool1)  # Output: True
print(bool2)  # Output: False

A = True # True value is treated as 1 in arithmetic operations
B = True
C = False # False value is treated as 0 in arithmetic operations

A + B + C # Output: 2 (1 + 1 + 0) Because True is 1 and False is 0
print(A + B + C)  # Output: 2


"""  <------------------- Null Data -------------------->
In programming, null represents the absence of a value or a non-existent value. In Python, the equivalent of null is None. It is used to indicate that a variable does not have any value assigned to it."""

# Example of Null:
null_var = None # Always None with a capital 'N'
print(type(null_var))  # Output: <class 'NoneType'>
print(null_var)  # Output: None
# None is often used to signify 'no value' or 'nothing here' in various programming scenarios.



# Extra Variables declareration examples:
x, y, z = 5, 10.5, "Hello"  # Multiple variable declaration in a single line
print(x)  # Output: 5
print(y)  # Output: 10.5
print(z)  # Output: Hello
# You can also assign the same value to multiple variables in a single line:
a = b = c = 100
print(a)  # Output: 100
print(b)  # Output: 100
print(c)  # Output: 100








