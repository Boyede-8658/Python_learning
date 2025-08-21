# Try and use while True for validation

while True:
    age = input("Enter your age: ")
    if age.isdigit():
        print(f"Your age is {age}")
        break
    else:
        print("Invalid input. Please enter a number.")
#         Enter your age: 22
# Your age is 22