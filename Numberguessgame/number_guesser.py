import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit(): #ensure input is a digit
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number greater than 0 next time :)")
        quit()
else:
    print("Please type a number next time :)")
    quit()
#random.randrange(start, stop) or randint
#r = random.randrange(1, 21)
#print(r)

random_no = random.randint(0, 10)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit(): #ensure input is a digit
        user_guess = int(user_guess)
    else:
        print("Please type a number next time :)")
        continue #brings us back to the top of loop

    if user_guess == random_no:
        print("Yay! You got it!")
        break
    elif user_guess > random_no:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")