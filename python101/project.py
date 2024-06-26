import random

def getRandomChoice():
    return random.choice(["Rock", "Paper", "Scissors"])

choicesDict = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors"
}

while True:
    print("1. r for Rock")
    print("2. p for Paper")
    print("3. s for Scissors")
    print("4. exit")
    choice =  input("Enter your choice: \n").lower()
    randomChoice = getRandomChoice()    

    if choice == 'stop':
        print("The game has been stopped")
        break
    # elif choice in choicesDict:
    elif choicesDict.get(choice, None):
        if choicesDict[choice] == randomChoice:
            print("You tied!!")
            continue
        elif (choice == 'r' and randomChoice == 'Scissors') or (choice == 'p' and randomChoice == 'Rock') or (choice == 's' and randomChoice == 'Paper'):
            print(f'You won!! YOUR {choicesDict[choice]} destroyed the {randomChoice}')
            play_again = input("Play again?(Y/N): ")
            if play_again.lower() == 'y':
                continue
            else:
                break
        else:
            print(f"You failed: The {randomChoice} destroyed YOUR {choicesDict[choice]} Try again!")
            continue
    else:
        print("Input is wrong, please type r, p, s, or stop!")
        continue    
