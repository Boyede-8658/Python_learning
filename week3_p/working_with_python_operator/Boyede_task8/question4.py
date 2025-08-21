student = {}
name = input('Enter name here: ')
age = int(input('Enter age here: '))
score = [70, 85, 90]
average_score = 82
student ={
    "name": name,
    "age": age,
    "scores": [70, 85, 90],
    "passed": average_score >50,
    "teenager": (age >=13) and (age <=19)
}
average_score = 82
passed = average_score >= 50
teenager = (age > 13) and (age <=19)
teenaqge = teenager == (age <= 13) and (age <=19)
print("student record")
print("name:", name)
print("age:", age)
print("scores:", score)
print("passed:", passed)
print("teenager:", teenager)