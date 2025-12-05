# A simple funciton with no parameters
def greet():
    print("Wlcome to the program!")


# A function with paramters
def add(a, b):
    return a + b # Send a value back to the caller
    
# A function that uses input and output inside 
def ask_and_square():
    x = int(input("Enter a number: "))
    return x * x

# Using the functions
greet()

result = add(5,7)
print("5 + 7", result)


square = ask_and_square()
print("Squared result =", square)
