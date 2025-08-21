# Try and think through this...
while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        print("Hello")
    elif choice == "2":
        print("Goodbye")
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
#         Menu:
# 1. Say Hello
# 2. Say Goodbye
# 3. Exit