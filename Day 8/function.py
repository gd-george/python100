def greet():
    print("Hello, welcome to Day 8!")


greet()

#function that allows input

def greet_with_name(name):
    print(f"Hello, {name}! Welcome to Day 8!")  


greet_with_name("George")

#function with more than 1 input

def greet_with(name, location):
    print(f"Hello, {name}! Welcome to {location}!")

greet_with("George","Port Blair")

#positional argument

greet_with(location="Port Blair", name="George")