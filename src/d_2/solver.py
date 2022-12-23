def getWin(x, y):
    opponentChoice = convertValue(x)
    myChoice = convertValue(y)

    if opponentChoice == myChoice:
        return 3
    else:
        if opponentChoice == 1:
            if myChoice == 2:
                return 6
            else: 
                return 0
        elif opponentChoice == 2:
            if myChoice == 1:
                return 0
            else:
                return 6
        else:
            if myChoice == 1:
                return 6
            else:
                return 0

def convertValue(val):
    '''
    This function converts the values passed in to 
    a common mapping:
    - 1 for rock
    - 2 for paper
    - 3 for scissors

    I found it easier to convert the values into shared values
    for part 1. For part 2, the mappings change obviously
    '''
    if val == "A" or val == "X":
        return 1
    elif val == "B" or val == "Y":
        return 2
    else:
        return 3

def getOutcome(x):
    if x == "X":
        return 0
    elif x == "Y":
        return 3
    else: 
        return 6

def findSolution(opponentsHand, outcome):
    oppHand = convertValue(opponentsHand)
    if outcome == "Y":
        return oppHand 
    elif outcome == "X":
        if oppHand == 1:
            return 3
        elif oppHand == 2:
            return 1
        else:
            return 2
    else: 
        if oppHand == 1:
            return 2
        elif oppHand == 2:
            return 3 
        else:
            return 1

# first read in the file information
with open("./input.txt", 'r') as file:
    lines = file.readlines()

# iterate over each pair, and calculate the value
# that we would get from playing that hand
sum1 = 0
sum2 = 0
for line in lines:
    firstLetter = line.split(" ")[0].strip()
    secondLetter = line.split(" ")[1].strip()

    # these are the answers to part 1 and 2 respectively
    sum1 += getWin(firstLetter, secondLetter) + convertValue(secondLetter)
    sum2 += getOutcome(secondLetter) + findSolution(firstLetter, secondLetter) 
print(sum1) 
print(sum2)


