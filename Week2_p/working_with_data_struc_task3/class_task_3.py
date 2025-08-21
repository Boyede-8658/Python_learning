#Write a program to take a string input from the user and display it in uppercase
name = "Adeoye Mary"
print(name.upper())

#given THE STRING "python",print its first and last characters
word = "Python"
print(word[::5])

#Ask the user for their name and print "Hello," where is the user's input
name = input("kindly input your name")
print(f"Hello, where is {name}")

#Write a program to count the number of characters in a string without using len()
text = "my day was stressful"
character = 0
print(character)


#Given "Hello World", replace "World" with "Python"
message = "Hello World"
print(message.replace("Hello World", "python"))

# Check if the given string contains the substring"python" (case-insensitive)
test = "python programming"
print("python" in test)
print("java" not in test)

#Write a program to reverse a string without using ([:-1])
happy= reversed("guess you are fine")
happy_j = "".join(happy)
print(happy_j)
#Given a string with extra spaces, remove the leading and trailing spaces
text = " Hello, how are you doing "
print(text.strip())

#Ask the user to enter a sentence and print the number of vowel in it
sentence =  input("kindly input a word: ").lower()
vowel_a = sentence.count("a")
vowel_e = sentence.count("e")
vowel_i =sentence.count("i")
vowel_o = sentence.count("o")
vowel_u = sentence.count("u")
total = vowel_a + vowel_e + vowel_i + vowel_o + vowel_u
print(total)

#Convert a string "123" to an integer and multiply it by 2
string ="1234"
multiply=int(string)
print(multiply*2)

# Given "Apple,banana,orange", split the string into a list of fruits
fruits = "apple banana orange"
print(fruits.split())

# Ask the user for a sentence and print each words on a new line
sent_1 = input("kindly input a sentence:")
sent_2= "\n".join(sent_1.split()) 
print(sent_2)

# Replace all spaces in a string with underscores()
word = "The lord is good"
print(word.replace("","_"))

# Count how many times the letter"a" appears in "Banana".
word = "banana"
print(word.count("a"))

# Check if a given string starts with "https.//".
string = "https://gmail.com"
print(string.startswith("https://"))