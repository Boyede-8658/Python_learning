# #Code along
# #see examples of use here

# #Range()
# for i in range(3):
#     print(i)
#     # output 
#     # 0 
#     # 1 
#     # 2

# #zip()
# names = ["Ester", "Precious", "Kennie"]
# scores = [85, 90, 75]
# for n, s in zip(names, scores):
#     print(n, "scored", s)
# # output
# # Ester scored 85
# # Precious scored 90
# # Kennie scored 75

# # its okay if you dont know what lambda is or how to use it.
# #map()
# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, nums))
# print(squared) #output [1, 4, 9, 16]

# #filter()
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums) #output [2, 4]


# # Student performance and feedback system
# # step 1: input student data
# name1 = input("Enter first student name: ")
# score1 = int(input("Enter score for " + name1 + ": "))

# name2 = input("Enter second student name: ")
# score2 = int(input("Enter score for " + name2 + ": "))

# name3 = input("Enter third student name: ")
# score3 = int(input("Enter score for " + name3 + ": "))

# # step2: store in lists
# names = [name1, name2, name3]
# scores = [score1, score2, score3]

# # step3 Display data
# print("\nStudent Data: ")
# for index, (n, s) in enumerate(zip(names, scores)):
#     print(f"{index + 1}. {n} - {s}")

# #step4: summary using built-ins
# total = sum(scores)
# average = round(total / len(scores), 2)
# highest = max(scores)
# lowest = min(scores)

# print("\nPerformance summary: ")
# print("Total scores:", total)
# print("Average score:", average)
# print("Highest score:", highest)
# print("Lowest score:", lowest)

# #step5: Rnking (using sorted and zip)
# ranked = sorted(zip(scores, names), reverse=True)
# print("\nRanking:")
# for rank, (score, name) in enumerate(ranked, 1):
#     print(f"{rank}. {name} - {score}")

# #step6: check data types
# print("\nData type checks:")
# print("Type of names:", type(name))
# print("Type of scores:", type(scores))
# print("ID of names list:", id(scores))

# #Step 7: Filter passing students (>=50)
# passing = list(filter(lambda s: s >= 50, scores))
# print("\nPassing scores:", passing)

# #Step 8: Map names to uppercase
# upper_names = list(map(lambda n:n.upper(), names))
# print("Uppercase Names:", upper_names)
# #step 9: use help()to show documentation of len
# print("\nHelp on len():")
# help(len) 
# # OUTPUT 
# # Enter first student name: Abiodun
# # Enter score for Abiodun: 90
# # Enter second student name: Steve
# # Enter score for Steve: 99
# # Enter third student name: Boye
# # Enter score for Boye: 40

# # Student Data:
# # 1. Abiodun - 90
# # 2. Steve - 99
# # 3. Boye - 40

# # Performance summary:
# # Total scores: 229
# # Average score: 76.33
# # Highest score: 99
# # Lowest score: 40

# # Ranking:
# # 1. Steve - 99
# # 2. Abiodun - 90
# # 3. Boye - 40

# # Data type checks:
# # Type of names: <class 'str'>
# # Type of scores: <class 'list'>
# # ID of names list: 2639751783168

# # Passing scores: [90, 99]
# # Uppercase Names: ['ABIODUN', 'STEVE', 'BOYE']

# # Help on len():
# # Help on built-in function len in module builtins:

# # len(obj, /)
# #     Return the number of items in a container.

# #function with arguement - the placeholder
# def greet(name):
#     print("Hello", name, "welcome to Python learning!")

# #Call with parameter- the actual name
# greet("Class rep")
# greet("Ridwan") 
# #Output 
# # Hello Class rep welcome to Python learning!
# # Hello Ridwan welcome to Python learning!

# print()
# def greet(name):
#     print("Hello", name)
# #funtion call
# result = greet("Esther")
# #You will notice that it did not store the name
# print("Result:", result)
# #output
# # Hello Esther
# # Result: None

# #RETURN()
# def add(a, b):
#     return a + b
# #function call
# result = add(4, 6)
# print("The sum is:", result) #The sum is: 10
# #note the output and compare it with that of print()

# #YIELD()
# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i # pause and return i
#         i += 1

# # Using the generator
# for number in count_up_to(5):
#     print(number)
# #output
# # 1
# # 2
# # 3
# # 4
# # 5

# #function argument
# #positional argument
# def introduce(name, track):
#     print("My name is", name)
#     print("I am learning", track, ".")

# #function call
# introduce("Ngozi", "AI Developer")  #correct order

# #Change the arrangement and watch the output
# introduce("AI Developer", "Ngozi") # incorrect order, this will throw a sematic error
# #outcome
# # My name is Ngozi
# # I am learning AI Developer .
# # My name is AI Developer
# # I am learning Ngozi .

# #Keyword Arguments
# def introduce(name, track):
#     print("My name is", name)
#     print("I am learning", track, ".")
# #Function call
# introduce(name = "Ngozi", track = "AI Developer")
# # Change the arrangement and watch the output
# introduce(track = "AI Developer",name = "Ngozi") # here you noice that the order does not matter
# #Output 
# # My name is Ngozi
# #I am learning AI Developer .

# #Default Arguments
# def introduce(name, track = "AI Developer"):
#     print("My name is", name)
#     print("I am learning", track,".")
# #function call
# # without specifying the default argument, but watch the output
# introduce("Paul") 
# #output
# # My name is Paul
# #I am learning AI Developer .

# # Specify the default argument and watch the output
# introduce(name = "Tunji Paul", track = "AI Developer")
# # output
# # My name is Tunji Paul
# # I am learning AI Developer.

# #VARYING LENGHT ARGUMENT
# def add_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     print("Sum:", total)
# #function call
# #take note of the output
# add_numbers(2, 4, 6)
# add_numbers(10, 20, 30, 40, 50) #Output Sum: 12 Sum: 150

# #Keyword argument (Dictionary)
# def student_details(**Kwargs):
#     for key, value in Kwargs.items():
#         print(key, ":", value)
# #Function call - Take note of the output
# student_details(name="Peter", track = "AI Developer", interest="Block chain")
# #Output
# # name : Peter
# # track : AI Developer
# # interest : Block chain

# #DEFINE STUDENT PROFILE FUNCTION
# #Ensure to not the order of arrangement of the types of arguments used.
# # This is how to arrange it or you are using everything or some of them together
# def participant_profile(name, age, track="AI Development", *skills, **extra_info):
#     """
#     Generate a profile for a bootcamp perticipant using different types of arguments
#     """
#     profile = f"\n--- Bootcamp perticipant profile ---\n"
#     profile += f"Name: {name}\n"
#     profile += f"Age: {age}\n"
#     profile += f"Track: {track}\n"

#     #skills (from *args)
#     if skills:
#         profile += "Skills: " + ", ".join(skills) + "\n"
#     else:
#         profile += "Skills: not yet specified\n"
#     #Extra info (from **kwargs)
#     if extra_info:
#         profile += "Additional info:\n"
#         for key, value in extra_info.items():
#             profile += f" - {key.capitalize()}: {value}\n"
#     return profile # Do you remember `return` and why it is used? We are using it so it can be reused in other places
# #Example 1: Using only positional arguments
# print(participant_profile("Peter", 24))
# #output
# # --- Bootcamp perticipant profile ---
# # Name: Peter
# # Age: 24
# # Track: AI Development
# # Skills: not yet specified

# # Example 2: Adding keyword/default argument
# print(participant_profile("Ridwan", 29, track="AI Engineering"))
# # --- Bootcamp perticipant profile ---
# # Name: Ridwan
# # Age: 29
# # Track: AI Engineering
# # Skills: not yet specified

# # Example 3: Adding variable-length positional arguments (*args)
# print(participant_profile("David", 27, "Data Science", "Python", "SQL", "Machine Learning"))
# # --- Bootcamp perticipant profile ---
# # Name: David
# # Age: 27
# # Track: Data Science
# # Skills: Python, SQL, Machine Learning
# # Example 4: Adding variable-length keyword arguments (**kwargs)
# print(participant_profile(
#     "Sophia", 30, "Cybersecurity",
#     "Networking", "Ethical Hacking", "Python",
#     interest="Blockchain", city="Shagamu", phone="08123456789"
# ))
# #output
# # --- Bootcamp perticipant profile ---
# # Name: Sophia
# # Age: 30
# # Track: Cybersecurity
# # Skills: Networking, Ethical Hacking, Python
# # Additional info:
# #  - Interest: Blockchain
# #  - City: Shagamu
# #  - Phone: 08123456789


# #NAMESCAPES AND SCOPE
# #Global namespace
# employee = "General Employee"
# def IT_department():
#     # Local Namespace inside IT_department
#     emloyee = "Chris (IT)"
#     print("Inside IT Department:", employee)
# def Training_department():
#     #local namespace inside IT_department
#     employee = "Chris (Training)"
#     print("Inside Training Department:", employee)
# print("In Global Namespace:", employee) # Refers to global variable
# IT_department() # Uses local variable in IT
# Training_department() #Uses local variable in training
# #Using a built-in namespace function
# print("Lenght of 'python':", len("Python"))
# #so, 'chris' can exist in more than one namespace without conflict.
# #please, take your time to study the output carefully.
# #OUTPUT
# # In Global Namespace: General Employee
# # Inside IT Department: General Employee
# # Inside Training Department: Chris (Training)
# # Lenght of 'python': 6


# # **Scope**
# # Scope defines where in the code a name is accessible.
# # Python follows the *LEGB Rule* (order of search for a variable):
# # L – Local → Inside the current function.
# # E – Enclosing → Inside any enclosing function(s).
# # G – Global → At the top level of the script/module.
# # B – Built-in → Python’s built-in functions/objects.
# x = "global x"   #Global Namespace
# def outer():
#     x = "enclosing x" #Enclosing Namespace
#     def inner():
#         x = "local x" #local Namespace
#         print("inside inner:", x)  #Local wins
#     inner()
#     print("in global:", x)  #Enclosing
# outer()
# print("in global:", x) #Global
# #watch the output
# #Notice how python searches in the order local = enclosing = global = built-in  (LEGB)
# #OUTPUT
# # inside inner: local x
# # in global: enclosing x
# # in global: global x


# #Global keyword
# #Used when you want to modify a global variable inside a function.
# x = 5
# def change_global():
#     global x
#     x = 10  # modifies the global x
# change_global()
# print(x)  # output: 10

# #nonlocal keyword
# #used in nested functions when you want to  modify the variable from the enclosing scop (not global).
# def outer():
#     x = "outer x"

#     def inner():
#         nonlocal x 
#         x = "changed by inner"
#         print("inside inner:", x)

#     inner()
#     print("inside inner:", x)

# outer() 
# #outcome
# # inside inner: changed by inner
# # inside inner: changed by inner

# #Lambda argument
# # You use lambda;
# # - When you need a short, throwaway function(not reuseable).
# # - To avoid writing full def functions for small tasks.
# # - Used with functions like map(), filter(), sorted(), and reduce().

#Normal function
def square(x):
    return x ** 2
# Lambda function
square_lambda = lambda x: x ** 2

print(square(5))
print(square_lambda(5))
#output
# 25
# 25

#this one has more than one arguments
add = lambda a, b: a + b
print(add(3, 7)) #outcome: 10

#let us lambda to apply the square function to a list
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares) #[1, 4, 9, 16]

#Let use lambda to filter even numbers
numbers = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens) # outcome: [10, 20, 30]

# Lets use lambda to sort the tuple within a list.

students = [("Ayo", 20), ("Bola", 18), ("Chika", 22)]
# Sort by age
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)

  
# Output: [('Bola', 18), ('Ayo', 20), ('Chika', 22)]

students_sorted_descending = sorted(students, key=lambda student: student[1], reverse=True)
print(students_sorted_descending)

# Output: [('Chika', 22), ('Ayo', 20), ('Bola', 18)]

students_sorted_alphabetically = sorted(students, key=lambda student: student[0])
print(students_sorted_alphabetically)

# Output: [('Ayo', 20), ('Bola', 18), ('Chika', 22)]
