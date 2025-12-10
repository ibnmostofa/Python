print ("Hello World")
a = 2
b = 8
if a < b:
    print ("a is less than b")
else:
    print ("a is not less than b")

d = int(input("Enter a number: "))
c = int(input("Enter another number: "))
e = d + c
print ("The sum of the two numbers is: ", e)

x, y, z = map(int, input("Enter three numbers: ").split())
if x < y and x < z:
    print ("x is the smallest number")
elif y < x and y < z:
    print ("y is the smallest number")
else:
    print ("z is the smallest number")


