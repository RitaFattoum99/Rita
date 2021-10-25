# import sys

# try:
#     operation = input("Enter your operation: ")
#     num01 = int(input("Enter first number :"))
#     num02 = int(input("Enter second number :"))
# except ValueError:
#     print("Error: Invalid Input")
#     sys.exit(1)

# def sum (num01 , num02):
#     return (num01 + num02)

# def min (num01 , num02):
#     return num01 - num02

# def mult (num01 , num02):
#     return num01 * num02

# def div (num01 , num02):
#     try:
#         return num01 / num02
#     except ZeroDivisionError:
#         print("Error: cannot Divide by 0.")
#         sys.exit(1)

# if operation == "+":
#     print(sum(num01 , num02))

# elif operation == "-":
#     print(min(num01 , num02))

# elif operation == "*":
#     print(mult(num01 , num02))

# elif operation == "/":
#     print(div(num01 , num02))
# else:
#     print("sorry there is some error try agian")


# # /////////////////
# class Flight():
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.passengers = []

#     def add_passenger(self, name):
#         if not self.open_seats():
#             return False
#         self.passengers.append(name)
#         return True

#     def open_seats(self):
#         return self.capacity - len(self.passengers)


# flight = Flight(1)

# people = ["Shams", "Osama", "Ritta", "Humam", "Eyhab"]

# for person in people:
#     if flight.add_passenger(person):
#         print(f"Added {person} in the flight successfully!")
#     else:
#      print(f"No Available Seats for {person}")

from tkinter import *


class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='First number')
        self.lbl2 = Label(win, text='Second number')
        self.lbl3 = Label(win, text='Result')
        self.t1 = Entry(bd=3)
        self.t2 = Entry()
        self.t3 = Entry()
        self.btn1 = Button(win, text='Add')
        self.btn2 = Button(win, text='Subtract')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1 = Button(win, text='Add', command=self.add)
        self.b2 = Button(win, text='Subtract')
        self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)

    def add(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1+num2
        self.t3.insert(END, str(result))

    def sub(self, event):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1-num2
        self.t3.insert(END, str(result))


window = Tk()
mywin = MyWindow(window)
window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()