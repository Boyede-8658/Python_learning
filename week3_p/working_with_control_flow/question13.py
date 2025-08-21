# Understanding `while True`**
# - The while True: loop is an infinite loop — it keeps running forever until you explicitly stop it with a break statement or by exiting the program.
# - It is commonly used when
# - You don’t know in advance how many times you want the loop to run.
# - You want to keep asking the user for input until a valid condition is met.
# - You are building continuous programs like menus, login systems, or simulation
# while True:
#     # Code block
#     # Must include a break statement to stop

#keep asking the user for a name until they type EXIT
while True:
    name = input("Enter your name (type 'exit' to quit): ")
    if name.lower() == "exit":
        print("Goodbye!")
        break
    print(f"Hello, {name}")