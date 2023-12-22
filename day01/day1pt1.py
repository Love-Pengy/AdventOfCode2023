#we are given lines of numbers and letters and need to take the first and last numbers, then conjoin them to get the number of that line 
# after this we need to sum all of them and output that number
DEBUG = 0


def getFirst(string): 
    for i in range(0, len(string)): 
        if(string[i].isdigit()):
            return(string[i])

def getLast(string): 
    for i in reversed(range(0, len(string))): 
        if(string[i].isdigit()): 
            return(string[i])

f = open("input.txt", "r")

sum = 0
for line in f: 
    first = int(getFirst(line))
    last = int(getLast(line))
    num = (first * 10) + last
    print(f"{first=} {last=}")
    sum += int(num)

print(f"answer is {sum}!")
