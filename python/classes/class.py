# from os import name


# class Point ():
#     def __init__(self , input1 , input2):
#         self.x = input1
#         self.y = input2

# p = Point(8 , 2)

# print(p.x)
# print(p.y)


# # ///////////////////////////////////////////////

# class Flight ():
    # def __init__(self , capacity):
        # self capacity = capacity
        # self passengers = []

# def add_passengers (self ,name):
# #     if 
# def open_seats (self):
#     return self.capacity - len(self.passengers)

class Flight ():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []
    
def add_passenger(self, name):
    if not self.open_seats :
        return False
    
    self.passenger.append(name)
    return True 

def open_seats(self):
    return self.capasity - len (self.passenger) 

flight = Flight(5)

people = ["Rita", "Ali", "Reham", "Falak", "Twfik"]

for i in people:
    if flight.add_passenger(i):
        print(f"Added {i} in the flight successfully!")
    else:
        print(f"No Available Seat for {i}.")

