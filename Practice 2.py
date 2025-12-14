# pylint: disable=invalid-name
print("Hello World")
a = 2
b = 8
if a < b:
    print("a is less than b")
else:
    print("a is not less than b")

d = int(input("Enter a number: "))
c = int(input("Enter another number: "))
e = d + c
print("The sum of the two numbers is: ", e)

x, y, z = map(int, input("Enter three numbers: ").split())
if x < y and x < z:
    print("x is the smallest number")
elif y < x and y < z:
    print("y is the smallest number")
else:
    print("z is the smallest number")

# Practice of 12th December 2025

Name = "Sajim Ibn Mostofa"
print("My name is:", Name)
length = len(Name)
print(length)
print("First Name:", Name[0:5])
print("Last Name:", Name[6:17])

# Escape Sequences
#    \n	New line
#    \t	Horizontal tab
#    \\	Backslash (\) print করে
#    \'	Single quote print করে
#    \"	Double quote print করে
#    \b	Backspace
#    \r	Carriage return
#    \f	Form feed
#    \a	Alert / Beep sound
print("Hello\nWorld")
print("Hello\tWorld")
print("I am Sajim\\Mostofa")
print('He said, \'Hello World\'')
print("She said, \"Hello World\"")
print("Hello\bWorld")
print("Hello\rWorld")
print("Hello\fWorld")
print("Hello\aWorld")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = f"{first_name} {last_name}"
print("My Name is:", full_name)
