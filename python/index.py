name = input("Enter Your Name :")
print(f"Hello {name}, You Are Welcome")
birth = int(input("Enter Your Birth date: "))
import datetime
today = datetime.datetime.now() 
print(f"You are {((today.year) - birth)} years old")
height = int(input("Enter Your Height: "))
weight = int(input("Enter Your Weight: "))
bmi = ((weight * 10000)/(height * height))
print(f"Your BMI is :{round(bmi ,2)}")

if bmi < 18.5:
    print("You are Underweight")
elif bmi <= 18.5 and 24.9:
    print("You are Normal")
elif bmi <= 25 and 29.9:
    print("You are Overweight")
else:
    print("You are Obese")