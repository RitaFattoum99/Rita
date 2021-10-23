import sys

try:
    operation = input("Enter your operation: ")
    num01 = int(input("Enter first number :"))
    num02 = int(input("Enter second number :"))
except ValueError:
    print("Error: Invalid Input")
    sys.exit(1)

def sum (num01 , num02):
    return (num01 + num02)

def min (num01 , num02):
    return num01 - num02

def mult (num01 , num02):
    return num01 * num02

def div (num01 , num02):
    try:
        return num01 / num02
    except ZeroDivisionError:
        print("Error: cannot Divide by 0.")
        sys.exit(1)

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


# /////////////////
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(1)

people = ["Shams", "Osama", "Ritta", "Humam", "Eyhab"]

for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} in the flight successfully!")
    else:
     print(f"No Available Seats for {person}")