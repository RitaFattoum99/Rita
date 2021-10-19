operation = input("Enter your operation: ")
num01 = int(input("Enter first number :"))
num02 = int(input("Enter second number :"))


def sum (num01 , num02):
    return (num01 + num02)

def min (num01 , num02):
    return num01 - num02

def mult (num01 , num02):
    return num01 * num02

def div (num01 , num02):
    return num01 / num02

if operation == "+":
    print(sum(num01 , num02))

elif operation == "-":
    print(min(num01 , num02))

elif operation == "*":
    print(mult(num01 , num02))

elif operation == "/":
    print(div(num01 , num02))
else:
    print("sorry there is some error try agian")


