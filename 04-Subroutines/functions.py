#Ex. 5: Define the display_university_address() function that displays university address. Then call the function two times.
def display_university_address():
    print("Cracow University of Economics\nRakowicka 27\n31-510 Krakow, POLAND")

for i in range(2):
    display_university_address()
print("-----------------")
#Ex. 6: Define a function that displays numbers in the layout as below (like on a phone keypad). Apply an loop statement. Then call the function.
#take 1
def print_keypad():
    for j in range(1,10):
        print(f"{j}", end = " ")
        if (j % 3 == 0):
            print()

#take 2
def print_keypad2():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for j in x:
        print(j, end = " ")
        if (j % 3 == 0):
            print()
#take 3
def print_keypad3():
    j = 1
    while (j < 10):
        print(j, end=" ")
        if(j % 3 == 0):
            print()
        j += 1

print_keypad()
print("-----------------")
print_keypad2()
print("-----------------")
print_keypad3()
print("-----------------")