a = int(input())
b = int(input())

for i in range(1,b):
    if i**2 >= a and i**2 <= b:
        print(i**2, end=" ")
