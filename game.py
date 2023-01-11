import random
answer = random.randint(1, 20)
while True:
    guess = int(input("Guess a number between 1 and 20: "))
    if guess == answer:
        print("Correct! The answer was", answer)
        break
    elif guess < answer:
        print("Too low.")
    else:
        print("Too high.")
