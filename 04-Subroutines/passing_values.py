#Ex. 7: Define a function multiplication(x, y) that displays the product of two numbers. Then call this function.
def multiplcation(x=3,y=4):
    print(f"{x} * {y} = {x * y}")

multiplcation(y=5)

#Ex. 8: Define a function that displays integer numbers from 1 to N. Then call the function and display numbers from 1 to 15.
def display_range(n=15):
    for i in range(1,n+1):
        print(i, end = " ")

display_range(int(input("Enter N [int]: ")))