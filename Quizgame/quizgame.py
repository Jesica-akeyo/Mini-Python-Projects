print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What are Monica and Ross' parents called? ")
if answer.lower() == "jack and judy":
    print("Yay thats Correct!")
    score += 1
else:
    print("sorry thats Incorrect!")

answer = input("Where do Rachel and Ross go on their first date? ")
if answer.lower() == "ross's museum":
    print("Yay thats Correct!")
    score += 1
else:
    print("sorry thats Incorrect!")

answer = input("Which character says the last ever line in the series? ")
if answer.lower() == "chandler":
    print("Yay thats Correct!")
    score += 1
else:
    print("sorry thats Incorrect!")

answer = input("Which song is Phoebe best known for? ")
if answer.lower() == "smelly cat":
    print("Yay thats Correct!")
    score += 1
else:
    print("sorry thats Incorrect!")

answer = input("What is Chandler's middle name? ")
if answer.lower() == "muriel":
    print("Yay thats Correct!")
    score += 1
else:
    print("sorry thats Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")

