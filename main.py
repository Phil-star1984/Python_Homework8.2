# This is a sample Python script.

secret = 13
guess = int(input("Guess a number between 0 and 20: "))

if guess < 0 or guess > 20:
    print("You stupid guy. The number has to be between 0 and 20")
elif guess > secret:
    print("Nope. This number is too high. Have another try.")
elif guess < secret:
    print("Nope. This number is too low. Have another try.")
elif guess == secret:
    print("Lucky Guy. You win!")
else:
    print("Malfunction.. go get some HELP!")

