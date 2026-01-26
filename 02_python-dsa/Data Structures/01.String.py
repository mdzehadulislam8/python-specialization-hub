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

