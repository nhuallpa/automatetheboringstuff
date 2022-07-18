import random

secret_number = random.randint(1,20)
counter = 1
print("I am thinking of a number between 1 and 20.")
print("Take a guess")
value = int(input())
while value != secret_number:
    counter+=1
    if value < secret_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    print("Take a guess")
    value = int(input())

print("Good job! You guessed my number in " + str(counter)+" guesses!")