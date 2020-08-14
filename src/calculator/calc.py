def add(v1, v2):
    print("Your answer is: " + str(v1 + v2))
    return


def sub(v1, v2):
    print("Your answer is: " + str(v1 - v2))
    return


def mul(v1, v2):
    print("Your answer is: " + str(v1 * v2))
    return


def div(v1, v2):
    print("Your answer is: " + str(v1 / v2))
    return


valid_input = False

num1 = float(input("Enter a number: "))
op = str(input("Enter an operator: "))
num2 = float(input("Enter a number: "))

while not valid_input:
    if op == "+":
        add(num1, num2)
        valid_input = True
    elif op == "-":
        sub(num1, num2)
        valid_input = True
    elif op == "x" or (op == "*"):
        mul(num1, num2)
        valid_input = True
    elif op == "/":
        div(num1, num2)
        valid_input = True
    else:
        op = str(input("Invalid operator!\nEnter a new operator: "))
