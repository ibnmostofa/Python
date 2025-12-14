# pylint: disable=invalid-name

# Practice of 12th December 2025
# Formatting Strings
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = f"{first_name} {last_name}"
# print("My Name is:", full_name)
print("My name is: ", full_name.title())
print(full_name.replace("a", "e"))
print(full_name.find(input("What index to find: ")))
