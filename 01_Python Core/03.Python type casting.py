"""Type Casting in Python
Type casting is the process of converting a variable from one data type to another. In Python,
 this can be done using built-in functions like int(), float(), str(), etc.
 """

# Type casting in Python is like exchanging currency when traveling between countries. Just as Bangladeshi Taka must be converted into US Dollars 
# to be used in America, one data type must be converted into another to work properly in Python. When you return, you convert it back again—this conversion 
# process is called type casting.

# Example of Type Casting:
# Converting Integer to String
num = 100
print(type(num))  # Output: <class 'int'>
num = str(num)
print(type(num))  # Output: <class 'str'> Here the integer 100 is converted to string '100'
print(num)  # Output: 100

# Converting Float to String
num2 = 30.05
print(type(num2))  # Output: <class 'float'>
print(num2)  # Output: 30.05
num2 = str(num2)
print(type(num2))  # Output: <class 'str'> Here the float 30.05 is converted to string '30.05'
print(num2)  # Output: 30.05

# Converting Float to Integer
num3 = 45.99
print(type(num3))  # Output: <class 'float'>
print(num3)  # Output: 45.99
num3 = int(num3)
print(type(num3))  # Output: <class 'int'> Here the float 45
print(num3)  # Output: 45

# Converting Integer to Float
num4 = 75
print(type(num4))  # Output: <class 'int'>
print(num4)  # Output: 75
num4 = float(num4)
print(type(num4))  # Output: <class 'float'> Here the integer 75
print(num4)  # Output: 75.0

# So in this way, type casting allows us to convert data from one type to another as needed in our programs.
# int(Variable nam), float(Variable name), str(Variable name) are the functions used for type casting in Python.
# Note : Type casting can sometimes lead to loss of data, especially when converting from float to int, as the decimal part is truncated.
# For example:
num5 = 9.99
print(type(num5))  # Output: <class 'float'>
print(num5)  # Output: 9.99
num5 = int(num5)
print(type(num5))  # Output: <class 'int'> Here the float 9.99 is converted to integer 9
print(num5)  # Output: 9
# In this case, the decimal part (.99) is lost during the conversion from float to int.


# Why need Type Casting?
# Type casting is essential in programming for several reasons:
# 1. Data Compatibility: Different operations and functions may require specific data types. Type casting
#    ensures that the data is in the correct format for processing.
# 2. Memory Management: Different data types consume different amounts of memory. Type casting can
#    help optimize memory usage by converting data to more efficient types when necessary.
# 3. User Input Handling: User inputs are often received as strings. Type casting is necessary to convert
#    these inputs into appropriate data types for calculations or processing.
# 4. Interfacing with External Systems: When interacting with databases, APIs, or
#    file systems, data may need to be converted to match the expected types of these systems.
# 5. Mathematical Operations: Certain mathematical operations require specific data types (e.g., integers
#    for counting, floats for precise calculations). Type casting ensures that these operations are performed correctly.
# 6. Avoiding Errors: Type mismatches can lead to runtime errors. Type casting helps prevent such errors
#    by ensuring that variables are of the expected type before performing operations on them.
# Overall, type casting is a fundamental aspect of programming that enhances code reliability, efficiency, and functionality.


# Type casting is a common practice: 
n = "100"
n2 = "60"
# Here n and n2 are strings. To perform addition, we need to convert them to integers.
sum_result = int(n) + int(n2)
print("The sum is:", sum_result)  # Output: The sum is: 160 
# Without type casting, the above operation would result in string concatenation instead of numerical addition.

