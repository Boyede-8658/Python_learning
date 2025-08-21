# 1. Take string input and display in uppercase
user_input = input("Enter a string: ")
print("Uppercase:", user_input.upper())

# 2. Print first and last character of "python"
s = "python"
print("First character:", s[0])
print("Last character:", s[-1])

# 3. Ask for name and greet
name = input("Enter your name: ")
print(f"Hello, {name}!")

# 4. Count characters without using len()
string_to_count = input("Enter a string to count characters: ")
count = 0
for _ in string_to_count:
    count += 1
print("Number of characters:", count)

# 5. Replace "World" with "Python" in "Hello World"
greeting = "Hello World"
updated_greeting = greeting.replace("World", "Python")
print("Updated greeting:", updated_greeting)


# 6. Check for "python" (case-insensitive)
text = input("Enter a string: ")
if "python" in text.lower():
    print("The string contains 'python'.")
else:
    print("The string does not contain 'python'.")

# 7. Reverse string without slicing
to_reverse = input("Enter a string to reverse: ")
reversed_str = ""
for char in to_reverse:
    reversed_str = char + reversed_str
print("Reversed string:", reversed_str)

# 8. Remove leading/trailing spaces
spaced_string = input("Enter a string with spaces: ")
print("Trimmed string:", spaced_string.strip())

# 9. Count vowels in a sentence
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
vowel_count = 0
for char in sentence:
    if char in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)

# 10. Convert "1234" to int and multiply by 2
num_str = "1234"
num = int(num_str)
print("1234 multiplied by 2:", num * 2)


# 11. Split "apple,banana,orange" into list
fruits = "apple,banana,orange".split(",")
print("Fruits list:", fruits)

# 12. Print each word on a new line
sentence_input = input("Enter a sentence: ")
words = sentence_input.split()
print("Words on new lines:")
for word in words:
    print(word)

# 13. Replace all spaces with underscores
original = input("Enter a string with spaces: ")
print("With underscores:", original.replace(" ", "_"))

# 14. Count "a" in "Banana"
word = "Banana"
a_count = word.lower().count("a")
print("Number of 'a's in 'Banana':", a_count)

# 15. Check if string starts with "https://"
url = input("Enter a URL: ")
if url.startswith("https://"):
    print("The string starts with 'https://'")
else:
    print("The string does not start with 'https://'")
