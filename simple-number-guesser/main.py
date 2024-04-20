import random

r = int(input("Enter range: "))
random_number = random.randint(0, r)
guesses = 0

while True:
    user_number = input("Guess a number or q to quit: ")

    if user_number == 'q':
        print("goodbye!")
        print(f"Your guesses: {guesses}")
        quit()
    elif user_number.isdigit():
        user_number = int(user_number)

    guesses += 1
    if user_number == random_number:
        print("You guessed it right!")
        continue
    elif user_number > random_number:
        print("You guessed it high")
        continue
    else:
        print("You guessed low")
        continue

