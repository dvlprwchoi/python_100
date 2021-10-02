from art import logo
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


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    should_continue = True
    for operator in operations:
        print(operator)

    while should_continue:
        operator = input("Pick an operation from the line above: ")
        # print(operations[operator])
        num2 = float(input("What's the next number?: "))
        operation_function = operations[operator]
        calculation = operation_function(num1, num2)
        print(f"{num1} {operator} {num2} = {calculation}")
        if input(f"Type 'y' to continue calculating with {calculation}, or type 'n' to exit.: ") == "y":
            num1 = calculation
        else:
            should_continue = False
            calculator()


calculator()
