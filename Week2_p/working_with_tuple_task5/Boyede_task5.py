#create and display
dish1 = input("Enter your favorite Nigerian dish: ")
dish2 = input("Enter your favorite Nigerian dish: ")
dish3 = input("input your favorite Nigerian dish: ")
dishes = (dish1, dish2, dish3)
print("Your favorite nigerian dishes are: " + ", ".join(dishes))
print("\nDishes one per line: ")
print("\n".join(dishes))

# Ask the user to enter 5 Nigerian states separated by commas
states_input = input("Enter 5 Nigerian states, separated by commas: ")
states_tuple = tuple(states_input.split(","))
states_tuple = tuple(state.strip() for state in states_tuple)
print("First state:", states_tuple[0])
print("Last state:", states_tuple[-1])
if "Lagos" in states_tuple:
    print("Yes, 'Lagos' is in the tuple.")
else:
    print("No, 'Lagos' is not in the tuple.")
print("Number of states entered:", len(states_tuple))


# Ask the user for their details
first_name = input("Enter your first name: ")
age = input("Enter your age: ")
favorite_color = input("Enter your favorite color: ")
home_town = input("Enter your home town: ")
profile = (first_name, age, favorite_color, home_town)
fname, age, color, town = profile
print("\n--- User Profile ---")
print(f"First Name:\t{fname}")
print(f"Age:\t\t{age}")
print(f"Favorite Color:\t{color}")
print(f"Home Town:\t{town}")

# Ask the user to enter 3 shopping items
items_input = input("Enter 3 shopping items, separated by commas: ")
shopping_list = tuple(item.strip() for item in items_input.split(","))
shopping_list_list = list(shopping_list)
extra_item1 = input("Enter an additional item: ")
extra_item2 = input("Enter another additional item: ")
shopping_list_list.append(extra_item1.strip())
shopping_list_list.append(extra_item2.strip())
updated_shopping_list = tuple(shopping_list_list)
print("\nUpdated Shopping List:")
print(" | ".join(updated_shopping_list))


# Store days of the week in a tuple
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
months_of_year = ("January", "February", "March", "April", "May", "June", 
                  "July", "August", "September", "October", "November", "December")
student_name = input("Enter student's name: ")
gender = input("Enter gender: ")
course_track = input("Enter course track: ")
while True:
    try:
        current_month_num = int(input("Enter current month number (1-12): "))
        if 1 <= current_month_num <= 12:
            break
        else:
            print("Please enter a valid month number between 1 and 12.")
    except ValueError:
        print("Please enter a number.")
while True:
    try:
        current_day_num = int(input("Enter current day number (1-7): "))
        if 1 <= current_day_num <= 7:
            break
        else:
            print("Please enter a valid day number between 1 and 7.")
    except ValueError:
        print("Please enter a number.")
current_month = months_of_year[current_month_num - 1]
current_day = days_of_week[current_day_num - 1]
print("\n--- Attendance Information ---")
print(f"Student Name:\t{student_name}")
print(f"Gender:\t\t{gender}")
print(f"Course Track:\t{course_track}")
print(f"Current Month:\t{current_month}")
print(f"Current Day:\t{current_day}")
