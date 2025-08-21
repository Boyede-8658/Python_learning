# Method 1 Using square brackets
empty_list = []
print(empty_list)  # Output []
https://github.com/dekpo23/Assignment/blob/main/Week%202/task5_solutions.py
#method 2
empty_list2 = list()
print(empty_list2) # Output []

# list of integers
numbers = [1, 2, 3, 4, 5]
print(numbers)   # output [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "cherry"]
print(fruits)   #output: ['apple', 'banana', 'cherry']

# Mixed_list
mixed_list = ["Alice", 25, 5.8, True]
print(mixed_list)  #output ['Alice', 25,5.8, True]

#form a string
chars = list("hello")
print(chars)   #Output: ['h', 'e', 'l', 'l', 'o']

my_tuple = (10,20,30)
list_from_tuple = list(my_tuple)
print(list_from_tuple)  #Outcome [10, 20, 30]

number_range =list(range(5))
print(number_range)  #Output:[0,1,2,3,4]

# squares of numbers 0-4
squares = [x**2 for x in range(5)]
print(squares)  #output: [0, 1, 4, 9, 16]

# Even numbers between 0-10
evens = [x for x in range(11) if x % 2 == 0]
print(evens)   #Output: [0, 2, 4, 6, 8, 10]

# Matrix-like list
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix)   # Output: [[1, 2], [3, 4], [5, 6]]

# Accessing elements in a nested list
print(matrix[0])   # output: [1, 2]
print(matrix[0][1])   # output 2

fruits = ["mango", "orange", "banana"]
print(fruits)    # ['mango', 'orange', 'banana']
print(fruits[0]) # mango  (first element)
print(fruits[2])      # banana (third element)

items = ["rice", "beans", "yam", "rice"]
print(items)  #['rice', 'beans', 'yam', 'rice']

numbers = [1, 2, 3]
numbers[1] = 20  # changing element at index 1
print(numbers)    # [1, 20, 3]

mixed = [10, "nigerian", 3.14, True]
print(mixed)  # [10, 'nigeria', 3.14, True]

nested_list = [[1, 2], ["a", "b"]]
print(nested_list)    # [[1' 2], ['a', 'b']]
print(nested_list[0][1]) #2

names = ["Ada"]
names.append("bola")
names.append("chidi")
print(names)  # ['Ada', 'Bola', 'chidi']