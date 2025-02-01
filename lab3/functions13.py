import random
def guess_the_number():
    name = input("Hello! What is your name?\n")

    #generating num
    num = random.randint(1, 20)
    attempts = 0
    guessed = False

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    print("Take a guess")

    while not guessed:
        guess = int(input())
        attempts += 1
        if guess < num:
            print("Your guess is too low.")
        elif guess > num:
            print("Your guess is too high")
        else:
            guessed = True
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")

guess_the_number()