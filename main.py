from operator import le
import random


def convertWord(word: str) -> dict:
    result = {}
    for i in range(len(word)):
        if word[i] in result:
            result[word[i]].append(i)
        else:
            result[word[i]] = []
            result[word[i]].append(i)
    return result


try:
    # state of the game
    wordList = []

    with open('words.txt', 'r') as file:
        f = file.readlines()
        for line in f:
            wordList.append(line[:-1])

    randomWord = random.choice(wordList)
    randomWordMap = convertWord(randomWord)

    wordProgress = ""

    for i in range(len(randomWord)):
        wordProgress += "_"

    state = 1
    print("Welcome to the Hangman game")

    usedLetter = set()
    while True:
        if state == 1:
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif state == 2:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif state == 3:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif state == 4:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif state == 5:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            # Game over, reset
            print("The word is: " + randomWord)
            print("Do you want to play again ? (y/n)")
            continueGame = input()
            if continueGame == "y":
                state = 1
                randomWord = random.choice(wordList)
                randomWordMap = convertWord(randomWord)
                wordProgress = ""
                usedLetter.clear()
                for i in range(len(randomWord)):
                    wordProgress += "_"
                continue
            elif continueGame == "n":
                print("Thanks for playing the game")
                break
        
        if len(usedLetter) != 0:
            allLetter = ""
            for letter in sorted(usedLetter):
                allLetter += letter 
                allLetter += " "
            print("You have used: " + allLetter)

        print(wordProgress)
        print()

        if (wordProgress == randomWord):
            print("You made it")
            print("Do you want to play again ? (y/n)")
            continueGame = input()
            if continueGame.strip() == "y":
                state = 1
                randomWordMap = random.choice(wordList)
                wordProgress = ""
                usedLetter = set()
                for i in range(len(randomWordMap)):
                    wordProgress += "_"
                continue
            elif continueGame.strip() == "n":
                print("Thanks for playing the game")
                break
            else:
                print("Wrong input, automatically stop")
                break
    
        userInput = input("Please enter a character: ")
        userInput = userInput.strip().lower()

        if len(userInput) != 1:
            print("Invalid input, try another character (you will be punished for it)")
            state += 1
            continue

        if userInput in usedLetter:
            print("You already use this letter, try another one")
            state += 1
            continue
        else:
            usedLetter.add(userInput)

        if userInput in randomWordMap:
            indexList = randomWordMap[userInput]
            for index in indexList:
                wordProgress = wordProgress[:index] + userInput + wordProgress[index + 1:]
            randomWordMap.pop(userInput)
        else:
            print()
            print("Wrong")
            state += 1
            continue

except FileNotFoundError:
    print("That file was not found")
