#What are Python decorators?
Ans: A decorator is a function that modifies the behavior of another function or class.
Syntax:
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper
@decorator
def say_hello():
    print("Hello!")

say_hello()
