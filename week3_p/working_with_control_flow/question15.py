for num in range(1, 6):
    if num == 3:
        continue
    print(num)
# 1
# 2
# 4
# 5
# 3 is skipped, but the loop continues.
## Some usecases
#Skip invalid data.
#Ignore unwanted characters (like spaces in a string).
#Continue running but avoid certain cases, etc.