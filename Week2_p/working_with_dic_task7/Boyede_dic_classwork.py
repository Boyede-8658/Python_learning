# Student bio data
student = {
    "name": "Steve",
    "age": 15,
    "course": "Biology Education"
}
print(student)

#using the dict() constructor
Student_info = dict(name="jonh", age=25, course="maths")
print(Student_info)

# Empty dictionary
Empty_dict = {}
print(Empty_dict)

#Dictionary comprehension
# {key_expression: value_expression for items in iterable if condition}
# Create a dictionary of numbers and their squares
squares = {x: x**2 for x in range(1, 9)}
print(squares)

# Dictionary of even numbers and their cubes
evens_cube = {x: x**3 for x in range(1, 10) if x % 2 == 0}
print(evens_cube)

#From Existing Dictionary
#Filter students who passed (score >= 50)
students = {"Ada": 85, "John": 40, "Musa": 65}
passed_students = {name: score for name, score in students.items() if score >= 50}
print(passed_students)


# using string keys
names = ["Ada", "John", "Musa"]
lengths = {name: len(name) for name in names}
print(lengths)   #output {'Ada': 3, 'John': 4' 'Musa': 4}

# Accesssing dictionary items
#Define a dictionary
student = {"name": "Ada", "Age": 20, "Course": "Computer science"}
print(student)

# using key
print(student["name"]) #output Ada

#using key
print(student["name"])

# Using get() method (avoids error if key is missing)
print(student.get("age"))
print(student.get("grade", "not found"))

# Modifying Dictionary
student["Age"] = 20 
student["Grade"] = "A"
#Removing items from dictionaries

# Using pop()
student.pop("Grade")
#using popitem() - removes last inserted key-value
student.popitem()
# Using del keyword
del student["course"]
print[student]
#using clear() - removes all items
student.clear()
print(student)


#Dictionary Methods
person = {"name": "Emeka", "Age": 30}
print(person.keys())
# value()
print(person.values())
# items()
print(person.items())
# update()
person.update({"Age": 31, "city": "lagos"})
print(person)

#Nested Dictionaries
#Accessing nested data
students = {
    "student1": {"name": "Ada", "age": 20},
    "student2": {"name": "John", "age": 22}
}
print(students["student1"]["name"])

#Looping through dictionaries
#Define a dictionary
student ={"name": "Ada", "Age": 20, "course": "Computer Science"}
print(student)
# Loop through keys
for key in student.keys():
    print(key)

# Loop through values
for value in student.values():
    print(value)

# loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}") #output name: Ada, Age 20, course: computer science

# Storing a student's biodata
student = {
    "name": "Chinedu",
    "age": 19,
    "department": "Engineering",
    "subjects": ["Maths", "Physics", "Chemistry"],
    "is_full_time": True
}
print(f"Name: {student['name']}")
print(f"Subjects: {', '.join(student['subjects'])}") #


# Create an empty dictionary
student = {}
# Add key-value pairs to it
student["name"] = "Goodness"
student["Interest"] = "AI"
student["Track"] = "AI_Dev"
print(student) #OUTCOME{'name":'Goodness', 'interest': 'AI', 'Track': 'AI_Dev'}

students = [
    {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
    {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
    {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
]
print(students[0]["Name"]) # outcome John
print(students[1]["Track"]) # outcome AI_Eng

students = {
    "AI010"  :  {"Name": "John","Interest": "AI", "Track": "AI_Dev"},
  "AI020" :  {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
  "AI030"  :  {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
}
print(students["AI020"]["Name"])   #outcome Mary
print(students["AI030"]["Track"])   # AI_Eng

students = {
    "AI010"  :  {"Name": "John","Interest": "AI", "Track": "AI_Dev"},
  "AI020" :  {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
  "AI030"  :  {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
}
print(students["AI020"]["Name"])   #outcome Mary
print(students["AI030"]["Track"])   # AI_Dev


scores = {
    "python": [85, 78, 92],
    "pandas": [88, 74, 90],
    "Scikit-learn": [80, 95, 87]
}
print(scores["python"])    #outcome 85, 78, 92
print(scores["pandas"][1])  #outcome 74

