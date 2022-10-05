# Let's define the functions we want the user to be able to perform.

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2


# Dictionary to store operation types
operations = {
    "+" : add, 
    "-" : subtract, 
    "*" : multiply, 
    "/" : divide
}

# Ask the user for the first number
num1 = int(input("Type in the first number:  "))

# Loop thorugh the dictionary to display the list of symbols for the user
for operation in operations:
    print(operation)

# Ask the user to pick an operation type
operation_symbol = input("Choose an operation type from the symbols above: ")

# Ask the user for the second number
num2 = int(input("\nType in the second number: "))

# Create a variable that picks a value from the operations dictionary based on the chosen user symbol
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

# Loop through the operations dictionary's keys (+, -, *, /)
for operation in operations:
    
    # If operation is equal to the operation_symbol chosen by the user print "answer"
    if operation == operation_symbol:
        print(f"\n{num1} {operation_symbol} {num2} = {answer}")

