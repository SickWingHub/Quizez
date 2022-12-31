print("Welcome to bible trivia!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What was the name of the first man? ")
if answer.lower() == "adam":
    print('Correct! ')
    score += 1
else:   
    print("Incorrect!")
    
answer = input("What was the name of his wife? ")
if answer.lower() == "eve":
    print('Correct!')
    score += 1
else:   
    print("Incorrect!")

answer = input("What is the name of God son? ")
if answer.lower() == "jesus":
    print('Correct!')
    score += 1
else:   
    print("Incorrect!")

answer = input("How many books are in the Bible? ")
if answer.lower() == "66":
    print('Correct!')
    score += 1
else:   
    print("Incorrect!")

answer = input("Who killed Abel? ")
if answer.lower() == "cain":
    print('Correct!')
    score += 1
else:   
    print("Incorrect!")

answer = input("Hho had the coat of many colors? ")
if answer.lower() == "joseph":
    print('Correct!')
    score += 1
else:   
    print("Incorrect!")

answer = input("How many plagues did God send to Egypt? ")
if answer.lower() == "10":
    print('Correct!')
    score += 1
else:   
    print("Incorrect!")

answer = input("Who got swallowed by a big fish? ")
if answer.lower() == "jonah":
    print('Correct!')
    score += 1
else:   
    print("Incorrect!")

answer = input("Who was a man after God's own heart? ")
if answer.lower() == "david":
    print('Correct!')
    score += 1
else:   
    print("Incorrect!")

answer = input("Who built an Ark? ")
if answer.lower() == "noah":
    print('Correct!')
    score += 1
else:   
    print("Incorrect!")

answer = input("Who parted the Red Sea? ")
if answer.lower() == "moses":
    print('Correct!')
    score += 1
else:   
    print("Incorrect!")

answer = input("What is the name of the first book of the Bible? ")
if answer.lower() == "genesis":
    print('Correct!')
    score += 1
else:   
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 12) * 100) + "%. ")