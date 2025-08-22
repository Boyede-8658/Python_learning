print("question 2 of task 8")
#Enter candidate info 
name = input(" Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your test score: "))

#Citizenship
Nationality = input("Enter your country: ")

institution =input(" Select your institution: ")
#Scholarship
scholarship = input('Do you have any other scholarship from oil and gas industries in Nigeria?(True or False) ')
#Academic Qualification
subjects = input('Enter subjects(including maths and English) seperated by commas: ')
grades = input('Enter grades for the subjects listed seperated by commas: ')

eligibility = (age < 18) and (score > 70) and (Nationality.title() == 'Nigeria') 
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")