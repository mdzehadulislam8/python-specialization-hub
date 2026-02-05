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
# Why instruction?
# Providing instructions helps guide the user on what kind of input is expected, making the interaction more user-friendly and reducing the chances of incorrect input.
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

# Now let’s focus on some solutions where, after taking input from the user, we need to handle various types of problems:
# Problem 1: Taking numerical input and performing arithmetic operations
num1 = input("Enter first number: ")  # Taking input as string  
num2 = input("Enter second number: ")  # Taking input as string
# Now, if we try to add these two inputs directly, it will concatenate them as strings instead of performing arithmetic addition.
print("Concatenated result:", num1 + num2)  # Output: Concatenated result: <num1><num2>
# For example, if the user enters 10 and 20, the output will be "1020" instead of 30.
# Solution: Solution is Type Casting ----->
# To perform arithmetic addition, we need to convert the string inputs to integers using type casting.
# Converting string inputs to integers for arithmetic operations
num1 = int(num1)
num2 = int(num2)
sum_result = num1 + num2  # Performing addition
print("Sum is:", sum_result)  # Output: Sum is: 30 (if inputs were 10 and 20)

# As a same way, we can also convert string inputs to floats for decimal arithmetic operations.

# Easy way type casting during input:
num3 = int(input("Enter a decimal number: "))  # Taking input and converting to int
num4 = float(input("Enter another decimal number: "))  # Taking input and converting to float
product = num3 * num4  # Performing multiplication
print("Product is:", product)  # Output: Product is: <calculated product>

# another example:
num5 = int(input("Enter an integer: "))  # Taking input and converting to int
num6 = int(input("Enter another integer: "))  # Taking input and converting to int
# Now If you get input float value like 5.5 it will give error because we are converting to int directly.
# So if you need float result then you can use float() function.
difference = num5 - num6  # Performing subtraction
print("Difference is:", difference)  # Output: Difference is: <calculated difference>

# Now If you select float type casting then you can get float result. and user 
# can also enter float value like 5.5 without error. also get integer value like 5.
num7 = float(input("Enter a number: "))  # Taking input and converting to float
num8 = float(input("Enter another number: "))  # Taking input and converting to float
division = num7 / num8  # Performing division
print("Division result is:", division)  # Output: Division result is: <calculated division>



# How to see Output in Python?
# In Python, you can see the output of your program in the console or terminal where you run your Python script. 
# When you use the print() function, it sends the output to the standard output stream, which is typically displayed in the console.
# Output -----to see------> print() <----- Print function # print("This is the output of the program.")  # Output: This is the output of the program.

# Comma Quotationn in print function:
# The comma in the print() function is used to separate multiple items that you want to print. When you use a comma, it automatically adds a space between the items in the output.
# print(Md. Zehadul Islam) # This will give an error because the name is not enclosed in quotes.
print("Md. Zehadul Islam")  # Output: Md. Zehadul Islam
print("Md.", "Zehadul", "Islam")  # Output: Md. Zehadul Islam
# In the second print statement, we are using commas to separate the three parts of the name, and Python will automatically add spaces between them in the output.

# Parameter in print function:
# print(object = separator = end = file = flush = ) # These are the parameters of print function

# Object: The object parameter is the value or values that you want to print. You can pass multiple objects separated by commas, and they will be printed with a space in between by default.
# Object - value(s) to be printed
print(40, 50, 60)  # Output: 40 50 60 # Here, we are passing three objects (40, 50, and 60) to the print function, and it will print them with spaces in between.
# We can print multiple objects within a single print function if we want.

# Separator: The separator parameter is used to specify a string that will be inserted between the objects when they are printed. By default, the separator is a space (' '), but you can change it to any string you like.
# Sep(Optional) - Allows us to separate multiple objeects inside print().
print("I", "love", "Python", sep="-")  # Output: I-love-Python # Here, we are using the separator parameter to specify that we want to separate the words with a hyphen (-) instead of a space.
print("I", "love", "Python", sep="*")  # Output: I*love*Python # Here, we are using the separator parameter to specify that we want to separate the words with an asterisk (*) instead of a space.
print("I", "love", "Python", sep="")  # Output: IlovePython # Here, we are using the separator parameter to specify that we do not want any separation between the words, so they will be printed together without spaces.

# end - Allows us to add specific values like new line, "\n" or Tab "\t" at the end of the print statement.
print("My name is Zehadu")
                           # <---- Here, the print statement will end with a new line by default, so the next print statement will be printed on a new line.
print("I love Python") 

print("My name is Zehadu", end=" ") 
                           # <---- Here, Output: My name is Zehadu I love Python # Here, we are using the end parameter to specify that we want to end the print statement with a space instead of a new line, so the next print statement will be printed on the same line.
print("I love Python") 

# file(Optional) - Where the values are printed. It's default value is sys.stdout(screen), which means the output will be printed to the console. However, you can change it to a file object to write the output to a file instead.
# flush(Optional) - boolean specifying if the output is flushed (True) or buffered (False). By default, it is set to False, meaning the output may be buffered for efficiency. If set to True, the output will be flushed immediately.

##### The next part will explain the file and flash in a better way.. because we need to know the loop to understand this, I will do it later.
# And these two are not used much. #####


# Now Let's see print input and output overall example  with formats and type casting:
first_number = int(input("Enter first number: "))  # Taking input and converting to int
second_number = int(input("Enter second number: "))  # Taking input and converting to int
sum_result = first_number + second_number  # Performing addition
# Displaying the result using formatted string
print("The First number is:", first_number)  # Output: The First number is: <first_number>
print("The Second number is:", second_number)  # Output: The Second number is: <second_number>
print("Sum is: ",{sum_result}) # Output: Sum is:  <sum_result>
# Most used print format:
print(f"The first number is: {first_number} \nThe second number is: {second_number} \nTotal Sum is: {sum_result}") # Output: The first number is: <first_number> The second number is: <second_number> Total Sum is: <sum_result>  
# another Style of print format:
print("The first number is: {} \nThe second number is: {} \nTotal Sum is: {}".format(first_number, second_number, sum_result)) # Output: The first number is: <first_number> The second number is: <second_number> Total Sum is: <sum_result>
# In this example, we take two numbers as input from the user, convert them to integers 

#### If you get new line then use ---> "\n" 
