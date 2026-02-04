"""<------------- Input and Output in Python --------------->"""

"""In Python, input and output operations are essential for interacting with users and displaying results.
Input refers to the data or information that a program receives from the user or another source, while output is the data or information that a program sends back to the user or another destination."""

"""
A real-life example is a smartphone camera app:

when you take a photo, the captured image is the input. The app processes the image (such as enhancing colors or detecting objects) and then shows the final 
edited photo on the screen as the output.
"""

# How to take Input in Python?
# In Python, you can take input from the user using the built-in input() function. This function reads a line of text entered by the user and returns it as a string.

# Example of taking input:
name = input("Enter your name: ")  # Prompt the user to enter their name
print("Hello, " + name + "!")  # Output a greeting message with the entered
# name
age = input("Enter your age: ")  # Prompt the user to enter their age
print("You are " + age + " years old.")  # Output the entered age
# Note: The input() function always returns the input as a string. If you need to work with other data types (like integers or floats), you may need to convert the input using type casting.

# How to display Output in Python?
# In Python, you can display output to the user using the built-in print() function. This function can print text, variables, and other data types to the console.
# Example of displaying output:
print("Welcome to Python programming!")  # Output a welcome message
number = 42
print("The answer to life, the universe, and everything is:", number)  # Output
# the value of the variable 'number'

# Without instruction:
user_input = input()  # Takes input from the user without any prompt
print("You entered:", user_input)  # Output the entered input

# With instruction:
user_input2 = input("Please enter something: ")  # Takes input with a prompt and showing instruction
print("You entered:", user_input2)  # Output the entered input and showing instruction
#Example:
a = input("Enter first number: ") # Taking input from user which shows instruction store in variable 'a'
b = input("Enter Last number: ") # Taking input from user which shows instruction store in variable 'b'
# After running the code then showing "Enter first number: " and "Enter Last number: " instructions to the user
# Then user will enter the values
# Finally, print the values with instruction
print("First number is:", a) # Output: First number is: <value of a>
print("Last number is:", b) # Output: Last number is: <value of b>

