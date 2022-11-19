arr = [[2,5,4],[9,0,3]]
#pp. a: the array
print(arr)
#pp. b: size of the array (number of rows and columns)
print(f"rows: {len(arr)}, cols: {len(arr[0])}")
#pp. c: value 5 from the array
print(arr[0][1])
#pp. d: value 3 from the array
print(arr[1][2])
#pp. e: second row of the array as below:
for item in arr[1]:
    print(item, end=' ')
print()
#pp. f: all values from the array as below:
for y in arr:
    for x in y:
        print(x, end=' ')
    print()
#pp. g: last column of the array as below:
for y in arr:
    print(y[2])