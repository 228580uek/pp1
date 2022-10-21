from email.mime import base
from math import sqrt
from random import randrange
#Ex. 5:

print(type(50))
print(type(149.17))
print(type(4*7))
print(type(4.0 * 7))
print(type("University"))
print(type(True))
print(type(2 > 5))

#Ex. 6:
print(3 - 2 + 1)
print(5 + 10 * 5)
print(4 + 4 / 2 ** 2)
print(4 % 3 % 2 % 1)
print(1 + 2 % 3 ** 4 * 5)
print(True != False)

#Ex. 7:
n1 = 5
n2 = 1
n3 = 8
n4 = 6
n5 = 3

sum = n1 + n2 + n3 + n4 + n5
print(sum)

sum_squared = n1 ** 2 + n2 ** 2 + n3 ** n3 + n4 ** n4 + n5 ** n5
print(sum_squared)

quotient = n3 / n5
print(quotient)

print(n3 == n4)

#Ex. 8:
x = 7
y = 34
z = y
y = x
x = z
print(f"{x} {y}")

#Ex. 9:
#name = input("Enter your name: ")
#surname = input("Enter your surname: ")
#print(f"{name} {surname}")

#Ex. 10:
#integer1 = int(input("Enter an integer: "))
#integer2 = int(input("Enter an another integer: "))
#sum_of_integers = integer1 + integer2
#print(sum_of_integers)

#Ex. 11:
#name = "Bogdan"
#age = 43
#height = 167
#print(f"My name is {name}, I'm {age} years old, and my height is {height} cm")

#Ex. 12:
#example_integer = 513
#text = "The valuse is {example_integer}, and {example_integer} is its second power is {example_integer**2}"
#print(text.format(example_integer = 12))

#Ex. 14:
#temperature_celsius = float(input("Read temperature (Celsius): "))
#temperature_kelvin = 273.15 + temperature_celsius
#temperature_fahrenheit = temperature_kelvin * (9/5) - 459.67
#print(f"Celsius = {temperature_celsius}, Kelvin = {temperature_kelvin}, Fahrenheit = {temperature_fahrenheit}")

#Ex. 15:
print(15 + 38)
print(3 + 4) #integer
print(5 + 9) #integer
print(int(7 / 2)) #3
print(48 % 5) #3
print((8 + 7 + 4 + 2)/2) #10.5
print(2 ** 10) #1024
#sqrt = 7
print(80*0.25) # 20.0

#Ex. 16:
#55
#2
#-1
#256
#5.0
#0
#11
#True
#True
#False
#True
#False
#3
#31
#1

#Ex. 17:
#176 = 5.9
print("I am 176cm tall, i. e. 5 feet 9 inches.")

#Ex. 18:
#side_a = float(input("Enter a:"))
#side_b = float(input("Enter b:"))
#side_c = float(input("Enter c:"))
#p = (side_a + side_b + side_c)/2
#s = sqrt(p*(p-side_a)*(p-side_b)*(p-side_c))
#print(s)

#Ex. 19:
#weight = float(input("Enter your weight in kg: "))
#height = float(input("Enter your height in cm: "))
#bmi = weight/((height/100)*(height/100))
#print(bmi)

#Ex. 20:
first_throw = randrange(1, 7)
second_throw = randrange(1, 7)
third_throw = randrange(1, 7)
sum_of_throws = first_throw + second_throw + third_throw
print(f"First {first_throw}, second {second_throw}, third {third_throw}, sum {sum_of_throws}")

#Ex. 21:
#computer_throw = randrange(1, 7)
#print(computer_throw)
#user_guess = int(input("Guess the number: "))
#print(computer_throw == user_guess)

#Ex. 22:
base_price = 15.84
vat = float(int(15.84 * 0.23 * 100)/100)
print(f"Amount: {base_price} zł")
print(f"VAT 23%: {vat} zł")