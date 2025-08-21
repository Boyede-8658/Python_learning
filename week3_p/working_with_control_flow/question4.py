#Nested if
#placing an if inside another if.
age = 19
citizen = True

if age >= 18:
    if citizen:
        print("you can vote")
    else:
        print("you must be a citizen to vote")
else:
     print("too yount to vote") # you can vote # else you cannot vote