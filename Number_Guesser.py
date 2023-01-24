import random

top_of_range = input("Enter a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please enter a number greater than 0")

    else:
        number = random.randrange(0, top_of_range)
        count = 0
        while True:
            count += 1
            guess = int(input("Enter your guess: "))
            if(number == guess):
                print(f"You guessed it correct!! in {count} guesse(s), the number is {number}")
                break
            elif number > guess:
                print("Guess a greater number")

            else:
                print("Guess a smaller number")

else:
    print("Please enter a  positive number next time!")

