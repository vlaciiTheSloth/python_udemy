from os import system

def addition(n1, n2):
    """Adds two number together."""
    return n1 + n2

def substraction(n1, n2):
    """Substracts the second number from the first number."""
    return n1 - n2

def multiplication(n1, n2):
    """Multiplies two number together."""
    return n1 * n2

def division(n1, n2):
    """Divides the first number with the second number."""
    return n1 / n2

operations = {
    "+" : addition,
    "-" : substraction,
    "*" : multiplication,
    "/" : division,
}

run = True
restart = "n"

while run:
    if restart == "n":
        system("cls")
        first_num = 0
        first_num = float(input("What's the first number? "))

    for symbol in operations:
        print(symbol)

    op = str(input("Pick an operation: "))
    sec_num = float(input("What's the next number? "))
    result = operations[op](first_num, sec_num)

    print(f"{first_num} {op} {sec_num} = {result}")

    notvalid_restart = True
    while notvalid_restart:
        restart = str(input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")).lower()
        if restart == "y" or restart == "n":
            notvalid_restart = False
        else:
            print("Invalid response.")
            
    if restart == "y":
        first_num = result

