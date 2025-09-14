# This is my first python program
print("I like pizza!")
print("its really good!")

#Variable = A container for a value (string, integer, float, boolean)
#         = A variable behaves as if it was the value it contains

# Strings
first_name = "Patrick Star"
food = "krabby patty"
email = "Patrick_Star@KrustyKrab.com"

# Integers
age = 12
quantity = 3
num_of_employee = 15

# Float
Price = 12.99
gpa = 3.5
distance = 6.5

# Print Strings
print (f"Hello {first_name}")
print (f"you like {food}")
print (f"your email is {email}")

#note : f = f-string or formatted string literals

# Print Integers
print (f"you are {age} years old")
print (f"you are buying {quantity} items")
print (f"you have {num_of_employee} employee")

# Print Float
print (f"The price is ${Price}")
print (f"your gpa is {gpa}")
print (f"you ran {distance}")

# Boolean
# Boolean only  have 2 options = True or False


is_student = False   # or True
if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

for_sale = False # or False
if for_sale:
    print("This house is for sale!")
else:
    print("this house is NOT for sale")

is_online = True
if is_online:
    print("You are online!")
else:
    print("You are NOT online!")