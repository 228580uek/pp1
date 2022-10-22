#Ex. 9: Define a function that returns the product of two numbers. Use the function to calculate the expression 15 * 12. Then display the result.
def multiplication (x, y):
    return x * y

print(f"15 * 12 is {multiplication(15,12)}")

#Ex. 10: Define a function read_number() that returns an integer number entered from the keyboard. The function should print a text prompting user to enter the number 'Enter a number: '. Then use the function to read two numbers from the keyboard. Display their sum.
from retrun_values_2 import read_number

x1 = read_number()
x2 = read_number()
print("Summary: {0}".format(x1 + x2))