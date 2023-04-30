# Firas Yacoub
#date: 04/30/23

#program 1
print("hello world")

#program 2
name = input("What is your name? ")
print("Hello " + name + "! Nice to meet you.")
#program 3
name = input("What is your name? ")
if name == "Firas":
    print("Hello Firas! Nice to meet you.")
elif name == "Zoe":
    print("Hello Zoe! Nice to meet you.")
else:
    print("Sorry, I don't know you.")

#program 4
import math

name = input("What is your name? ")
radius = float(input("Enter the radius of the circle: "))

area = math.pi * (radius ** 2)

print("Hello " + name + "! The area of the circle is:", round(area, 2))
#program 5
name = input("What is your name? ")
miles = float(input("Enter the number of miles driven: "))
gallons = float(input("Enter the number of gallons used: "))

mpg = miles / gallons

print("Hello " + name + "! Your car gets", round(mpg, 2), "miles per gallon.")
#program 6
name = input("What is your name? ")
fahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print("Hello " + name + "! The temperature in degrees Celsius is:", round(celsius, 2))
#program 7
name = input("What is your name? ")
start_day = int(input("Enter the starting day number (0 for Sunday, 1 for Monday, etc.): "))
stay_length = int(input("Enter the length of your stay (in nights): "))

return_day = (start_day + stay_length) % 7

print("Hello " + name + "! You will return on day", return_day, "of the week.")

