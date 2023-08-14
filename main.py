# Calculator Project

from art import logo
import os
import time

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

# Square Root
def nth_root(n1, root):
    return n1 ** (1 / root)

# Exponent
def exponent(n1, n2):
    return n1 ** n2

# Check for System Environment
def is_windows():
    return os.name == "posix"

def is_linux():
    return os.name == "nt"

# Exiting Message
def display_exit_message():
    print("Exiting the calculator...")
    time.sleep(3)
    os.system("clear") if is_linux else os.system("cls")

# Restart Message
def display_restart_message():
    print("Restarting the calculator...")
    time.sleep(3)
    os.system("clear") if is_linux else os.system("cls")
    print("Bye bye!")
    
operations = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide,
"nth_root": nth_root,
"exp": exponent
}

def start_calculator():
    should_continue = True
    print(logo)
    
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        if operation_symbol == "nth_root":
            num2 = float(input("What's the root?: "))
        elif operation_symbol == "exp":
            num2 = float(input("What's the exponent to raise to?: "))
        else:
            num2 = float(input("What's the next number?: "))
        calc_func = operations[operation_symbol]
        result = calc_func(num1, num2)
        print(f"{num1:,} {operation_symbol} {num2:,} = {result:,}")
    
        while True:
            keep_calculating = input(f"Type 'y' to keep calculating with {result}, type 'n' to start a new calculation, or type 'quit' to exit the calculator: ")
            
            if keep_calculating == 'y' or keep_calculating == 'n' or keep_calculating == 'quit':
                break
            else:
                print("Please, provide a valid answer.")
    
        if keep_calculating == 'y':
            num1 = result
        elif keep_calculating == 'n':
            should_continue = False
            display_restart_message()
            start_calculator()
        else:
            should_continue = False
            display_exit_message()
            
start_calculator()