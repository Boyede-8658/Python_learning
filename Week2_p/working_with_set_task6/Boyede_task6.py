# Ask the user to enter 5 favorite fruits, separated by commas
fruits_input = input("Enter 5 favorite fruits, separated by commas: ")
fruit_set = set(fruit.strip() for fruit in fruits_input.split(","))
print("\nYour favorite fruits (as a set):")
print(fruit_set)

# Create an empty set to store unique names
attendees = set()
try:
    count = int(input("How many people are attending the seminar? "))
except ValueError:
    print("Please enter a valid number.")
    exit()
for i in range(count):
    name = input(f"Enter name of attendee {i + 1}: ").strip()
    attendees.add(name)  # Set ensures uniqueness
sorted_attendees = sorted(attendees)
print("\nList of unique attendees (alphabetical order):")
for name in sorted_attendees:
    print(name)

