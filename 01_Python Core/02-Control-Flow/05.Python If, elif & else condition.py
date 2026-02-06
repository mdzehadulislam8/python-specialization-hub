"""-------------> If Else Statements in Python <-----------------"""
# What is an If Else Statement?
# An if else statement is a control flow statement that allows you to execute different blocks of code
# based on certain conditions. It is used to make decisions in your code.

# Maintain some rules for using if else statements:
# 1. Every statement we follow indentation in Python. The code block inside the if, elif, and else statements must be indented.
# 2. The if statement is used to check a condition. If the condition is true, the code block inside the if statement will be executed.
# 3. The elif statement is used to check multiple conditions. It stands for "else if". You can have as many elif statements as you want.
# 4. The else statement is used to execute a block of code when all the previous

# If condition:
# If condiion you can show multiple statements inside the if condition. If the condition is true, all the statements inside the if block will be executed.

# If Conditions are False:
a = 0
if a > 0:
    print("My name is Zehad.")
# ^                                   # <--- If the if condition works (is true), then all the print statements inside the indentation will be executed.
# |  <-- Inside the indentation       # Otherwise, none of them will be executed.
# v  <--- area of the <if> condition  # This is because in an if condition, all the statements inside the indented block run together.
    print("This is a positive number.")
print("This is outside the if condition.") # <-- This statement is outside the if condition, so it will be executed regardless of whether the if condition is true or false.

# If Conditions are True:
a = 10
if a > 0:
    print("My name is Zehad.")
    print("This is a positive number.")
# In this case, since 'a' is greater than 0, both print statements inside the if condition will be executed.

# Else Conditions:
# The else statement is used to execute a block of code when the if condition is false.
# Example:
number = 50
if number < 0:
    print("This is a negative number.")
else:
    print("This is a positive number.")
# In this example, since the condition 'number < 0' is false, the code block inside the else statement will be executed.
# If condistion work then else will be skipped.
number = -10
if number < 0:
    print("This is a negative number.")
else:
    print("This is a positive number.")
# In this example, since the condition 'number < 0' is true, the code block inside the if statement will be executed, and the else block will be skipped.

# Elif Conditions:
# Why do we need elif statements? 
# We use elif statements when we want to check multiple conditions. It allows us to check for more than one condition without having to nest multiple if statements.
# Example:
score = input("Enter your score: ")
score = int(score)  # Convert the input to an integer
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:           # <---- Here every condition is checked in order, and the first condition that is true will be executed. If none of the conditions are true, the else block will be executed.
    print("Grade: C")
elif score >= 60:
    print("Grade: D")   
else:
    print("Grade: F")
# In this example, we check the score and assign a grade based on the value of the score.
# The elif statements allow us to check multiple conditions in a clear and organized way.

"""If-elif-else and nastad and if any logic becomes true then nothing else below it is checked and Python does not see it."""

# I am showing a real-life example of an if-elif–else condition:
"""📖 Story: Rahim Goes to School

Rahim wakes up in the morning and looks outside.

If it is raining, Rahim takes an umbrella.

Else if it is cloudy, Rahim takes a raincoat.

Else, the weather is sunny, so Rahim goes out normally."""

# Now, let's see how we can implement this story in Python using if, elif, and else statements.
# Example 1: Using if, elif, and else statements
weather = input("What is the weather like today? (rainy/cloudy/sunny): ")
if weather == "rainy":
    print("Rahim takes an umbrella.") 
elif weather == "cloudy":
    print("Rahim takes a raincoat.")
else:
    print("Rahim goes out normally.")
# In this example, we ask the user to input the weather condition. Based on the input, we use if, elif, and else statements to determine what Rahim should do.

# Example 2: If-elif-else with multiple conditions
f_game = input("Which football team do you support? (1. Brazil 2. Argentina or 3. France): ")
if f_game == "1":
    print("You support Brazil.")
elif f_game == "2":
    print("You support Argentina.")
elif f_game == "3":
    print("You support France.")
else:
    print("Invalid input. Please choose 1, 2, or 3.")
# In this example, we ask the user to input which football team they support. We use if, elif, and else statements to determine the user's choice and handle invalid input.

# Nasted If-elif-else:
# We can also nest if-elif-else statements inside each other to create more complex decision-making structures.
# It's a way to check multiple conditions in a hierarchical manner.
# Example:
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
    if age < 13:
        print("You are a child.")   # <--- This is a nested if statement. It checks if the age is less than 13, which is a more specific condition within the broader condition of being a minor.
                                    # Firstly check the condition. firstly if it is not true then it will skip the whole block of code. If it is true then it will check the next condition.
                                    # Which are nasted 
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")
# In this example, we first check if the age is less than 18. If it is, we print that the person is a minor. Then, we have another if statement nested inside the first one to check if the age is less than 13, which indicates that the person is a child.
# If the age is between 18 and 65, we print that the person is an adult. If the age is 65 or above, we print that the person is a senior. This demonstrates how we can use nested if-elif-else statements to handle more complex conditions.


