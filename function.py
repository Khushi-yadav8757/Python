#What is a Function?
A function is a block of code that performs a specific task.
It helps you reuse code, so you don’t need to write the same logic again and again.

#types of Functions in Python
Built-in Functions – Already provided by Python.
Examples: print(), len(), input(), range()

User-defined Functions – Functions that you create.
-------------------------------------------------------------------------------
#Syntax of a User-Defined Function
def function_name():

   # statements
  Example 1: Simple Function
def say_hello():
    print("Hello, Khushi!")
    say_hello()
  #Output: Hello, Khushi!
----------------------------------------------------------------------------
 Example 2: Function with Parameter
def greet(name):
    print("Good morning,", name)
greet("Khushi")
#Output: Good morning, Khushi

Example 3: Function with Return Value
def add(a, b):
    return a + b
result = add(5, 3)
print("Sum is:", result)
# Output: Sum is: 8
----------------------------------------------------------------------------
 Example 4: Function with Default Parameter
def welcome(name="Guest"):
    print("Welcome,", name)
welcome()         # Output: Welcome, Guest
welcome("Khushi") # Output: Welcome, Khushi

Example 5: Function with Multiple Parameters
def student_details(name, age, branch):
    print("Name:", name)
    print("Age:", age)
    print("Branch:", branch)
student_details("Khushi", 20, "CSE")

#Why Use Functions?
Increases code reusability
Makes code organized and clean
Easier to debug and maintain
Allows modular programming
