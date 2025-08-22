print("question 3 of task 3")
#User
while True:
 Name = input("Enter your name: ")
 if Name.lower() == "exit":
  print("Goodbye!")
  break
 print(f"Hello! {Name}")