# Idea here is to start from the beginning and find if there is a number after that check if there is a number spelled out before that point
# second part of idea: take all instances of word numbers and put it in a tuple array then delete everything but the first and last items and compare with the pure ints
# unthought of possibility: if a number is found first but is later in the string it will take that number first and cut form there
# solution: go through all of them at once and sort them after
DEBUG = 0


def parseStringToInt(string): 
    numList = list()
    cutIndex = 0
    parseString = string

    #hold = input("pause")
    if(len(parseString) == 0): 
        return(None)
    cutIndex = 0
    while(1): 
        if("one" in parseString): 
            numList.append((1, (parseString.index("one") + cutIndex)))
            cutIndex = (string.index("one") + 3)
            parseString = parseString[cutIndex:]        
        else: 
            break

    parseString = string
    cutIndex = 0
    while(1): 
        if("two" in parseString): 
            numList.append((2, (parseString.index("two") + cutIndex)))
            cutIndex = (string.index("two") + 3)
            parseString = parseString[cutIndex:]        
        else: 
            break
    
    cutIndex = 0
    parseString = string
    while(1): 
        if("three" in parseString): 
            numList.append((3, (parseString.index("three") + cutIndex)))
            cutIndex = (string.index("three") + 5)
            parseString = parseString[cutIndex:]        
        else: 
            break 

    cutIndex = 0
    parseString = string
    while(1): 
        if("four" in parseString): 
            numList.append((4, (parseString.index("four") + cutIndex)))
            cutIndex = (string.index("four") + 4)
            parseString = parseString[cutIndex:]        
        else: 
            break 
        
    cutIndex = 0
    parseString = string
    while(1): 
        if("five" in parseString): 
            numList.append((5, (parseString.index("five") + cutIndex)))
            cutIndex = (string.index("five") + 4)
            parseString = parseString[cutIndex:]        
        else: 
            break

    cutIndex = 0
    parseString = string
    while(1): 
        if("six" in parseString): 
            numList.append((6, (parseString.index("six") + cutIndex)))
            cutIndex = (string.index("six") + 3)
            parseString = parseString[cutIndex:]        
        else: 
            break

    cutIndex = 0
    parseString = string
    while(1): 
        if("seven" in parseString): 
            numList.append((7, (parseString.index("seven") + cutIndex)))
            cutIndex = (string.index("seven") + 5)
            parseString = parseString[cutIndex:]        
        else: 
            break

    cutIndex = 0
    parseString = string
    while(1): 
        if("eight" in parseString):
            numList.append((8, (parseString.index("eight") + cutIndex)))
            cutIndex = (string.index("eight") + 5)
            parseString = parseString[cutIndex:]        
        else: 
            break 
    
    cutIndex = 0
    parseString = string
    while(1): 
        if("nine" in parseString): 
            numList.append((9, (parseString.index("nine") + cutIndex)))
            cutIndex = (string.index("nine") + 4)
            parseString = parseString[cutIndex:]        
        else: 
            break 

    if(len(numList) == 0): 
        return(None)

    if(len(numList) == 1): 
        return(numList)


    if(len(numList) < 3): 
        if((numList[1][1]) < (numList[0][1])): 
            numList.reverse()
        return(numList)
    
    first = None
    last = None
    finalNumList = list()
    for i, element in enumerate(numList): 
        if(first is None): 
            first = element
            finalNumList.append(element)

        elif(last is None): 
            last = element
            finalNumList.append(element)
            if(finalNumList[1][1] < finalNumList[0][1]): 
                finalNumList.reverse()

        elif(element[1] < first[1]): 
            first = element
            finalNumList[0] = element

        elif(element[1] > last[1]): 
            last = element
            finalNumList[1] = element
        else: 
            continue
    return(finalNumList)

def getFirst(string): 
    for i in range(0, len(string)): 
        if(string[i].isdigit()):
            return((int(string[i]), i))
    return(None)

def getLast(string): 
    for i in reversed(range(0, len(string))): 
        print(string[i], i ,sep=' ', end='')
        if(string[i].isdigit()): 
            return((int(string[i]), i))
    return(None)

f = open("input.txt", "r")

sum = 0
test = 0
for line in f: 
    test += 1
    firstInt = getFirst(line)
    lastInt = getLast(line)
    wordList = parseStringToInt(line) 
    if(wordList is not None): 
        if(len(wordList) > 1): 
            firstWord = wordList[0]
            lastWord = wordList[1]
        else: 
            firstWord = wordList[0]
            lastWord = wordList[0]
    else: 
        firstWord = None
        lastWord = None
    

    print(f"{firstInt=}, {lastInt=}, {firstWord=}, {lastWord=}, {test=}")

    if((firstInt is not None) and (firstWord is not None)): 
        if(firstInt[1] < firstWord[1]): 
            firstNum = firstInt[0]
        else: 
            firstNum = firstWord[0]
    else: 
        if(firstInt is None): 
            firstNum = firstWord[0]
        else: 
            firstNum = firstInt[0]
    
    if((lastInt is not None) and (lastWord is not None)): 
        if(lastInt[1] > lastWord[1]): 
            lastNum = lastInt[0]
        else: 
            lastNum = lastWord[0]
    else: 
        if(lastInt is None): 
            lastNum = lastWord[0]
        else: 
            lastNum = lastInt[0]
    
    num = (firstNum * 10) + lastNum
    print(f"{firstNum=} {lastNum=} {test=}")
    sum += int(num)


print(f"answer is {sum}!")
