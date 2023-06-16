import random

wordArray = ["resin","shade","haunt","orate","alert"]
currentWord = wordArray[int(random.randint(0,(len(wordArray)-1)))]
userGuessArray = []
userGuessLetterArray = []
starMatrix = [
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"]
            ]
j = 0

while len(userGuessArray)<5:
    if len(userGuessArray) == 0:
        for i in starMatrix:
            print(i)
    else:
        userGuessLetterArray = []
        for letter in userGuessArray[j]:
            userGuessLetterArray.append(letter)
        starMatrix[j] = userGuessLetterArray
        j += 1
        for i in starMatrix:
            print(i)

    userInput = input("Enter a word: ")
    if len(userInput) == 5:
        if userInput == currentWord:
            print("Congratulations! You won in " + str(len(userGuessArray)) + " tries!")
            break
        else:
            userGuessArray.append(userInput)
    else:
        print("Enter a 5 letter word")

if len(userGuessArray)>=5:
    print("Oh no you lost. The word was: " + currentWord)
