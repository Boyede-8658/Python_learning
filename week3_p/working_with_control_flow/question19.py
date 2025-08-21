#lets make a guess
secret = "python"
while True:
    Guess = input("Guess the secret word: ")
    if Guess.lower() == secret:
        print("correct! you guessed right.")
        break
    else:
        print("wrong! try again.")