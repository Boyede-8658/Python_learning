# Your life favorite
favorite_quote = input("Enter your favorite quote: ")
quote_title = favorite_quote.title()
print("Your favorite life quote is: \"" + quote_title + "\"")

#shopping list manager
shopping_list =[]
item1 = input("Enter your first shopping: ")
item2 = input("Enter your second shopping item: ")
item3 = input("Enter your third shopping item: ")
shopping_list.append(item1)
shopping_list.append(item2)
shopping_list.append(item3)
print("Your shooping list: " + ",". join(shopping_list))
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words in the sentence:", len(words))


# Ask the user to enter 5 names separated by spaces
names_input = input("Enter 5 names separated by spaces: ")
names_list = names_input.split()
if len(names_list) != 5:
    print("Please enter exactly 5 names.")
else:
    for i in range(len(names_list)):
        names_list[i] = names_list[i].lower()
    names_list.sort()
    print("Sorted names:")
    for name in names_list:
        print(name)


# Create empty lists for names and scores
student_names = []
student_scores = []
for i in range(3):
    name = input(f"Enter the name of student {i + 1}: ")
    score = input(f"Enter the score for {name}: ")
    student_names.append(name)
    student_scores.append(score)
print("\nStudent Scores:")
print("---------------------")
for i in range(3):
    print(f"{student_names[i]:<10} — {student_scores[i]}")


#Ask the user to input a word
word = input("Enter a word: ")
print("Length of the word:", len(word))
if word.isupper():
    print("The word is in ALL UPPERCASE.")
elif word.islower():
    print("The word is in all lowercase.")
elif word.istitle():
    print("The word is in Title Case.")
else:
    print("The word is in mixed or other casing.")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)


#Create a list of five cities
cities = ["Abuja", "Lagos", "Abeokuta", "Ado", "Enugu"]
new_city = input("Enter a new city to replace the third one: ")
cities[2] = new_city
cities.pop()
start_city = input("Enter a city to add to the beginning of the list: ")
cities.insert(0, start_city)
print("\nUpdated list of cities:")
print(cities)