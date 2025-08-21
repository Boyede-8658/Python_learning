#Student bio data storage
name = input("name")
age = input("age")
gender = input("gender")
course = input("course")
value = dict(name =(name), age =(age), gender =(gender), course =(course))
print(value)
print("\n\t--- value ---")
print(f"\tname:\t\t{value['name']}")
print(f"\tage:\t\t{value['age']}")
print(f"\tgender:\t\t{value['gender']}")

# Super market price list
rice = input("price of rice: ")
beans = input("price of beans: ")
spagetti = input("price of spagetti: ")
items = dict(rice =(rice), beans =(beans), spagetti =(spagetti))
print(items)
rice2 = input("updated price ")
beans2 = input("updated price ")
spagetti2 = input("updated price ")
update =(rice2, beans2, spagetti2)
items.update(rice=(rice2), beans=(beans2), spagetti=(spagetti2))
print(items)

#task3: Days and activities pairing
# Step 1: Store days in a tuple
days = ("Monday", "Wednesday", "Friday")
activities = []
for day in days:
    activity = input(f"What activity do you have on {day}? ")
    activities.append(activity)
schedule = {day: activity for day, activity in zip(days, activities)}
print("\nYour weekly schedule:")
print(schedule)

#Task4 unique members registration
# Ask the user to enter three names separated by commas
input_names = input("Enter three names separated by commas: ")
# Split the names and convert them into a set to ensure uniqueness
set_of_names = set(input_names.split(","))
# Create a dictionary with names as keys and their lengths as values
name_length_dict = {name.strip(): len(name.strip()) for name in set_of_names}
# Output the resulting dictionary
print("Name and their lengths (unique):")
print(name_length_dict)


#Task5 contact quick lookup
names = ("favor", "oreoluwa", "victor")
phone_numbers = ("08066666666", "070555555555", "081000000000")
phone_book = dict(zip(names, phone_numbers))
search_name = input("enter a name to search for: "). capitalize()
numbers = phone_book.get(search_name,"name not found in phone book.")
print(numbers)