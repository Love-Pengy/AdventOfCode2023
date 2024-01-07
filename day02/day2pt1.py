with open("input.txt", "r") as f: 
    i = 0
    idSum = 0
    maxRed = 12
    maxGreen = 13
    maxBlue = 14
    invalid = False

    for line in f: 
        print(line)
        if(line == "\n"): 
            continue

        i += 1
        strLine = line.split(":")
        if(len(strLine) >= 2): 
            games = strLine[1].split(";")
        else: 
            games = strLine
        for rolls in games: 

            if(invalid): 
                break 

            singleColors = rolls.split(",")
            for color in singleColors: 
                if("red" in color): 
                    color = color.replace("red", "")
                    num = int(color)
                    if(num > maxRed): 
                        print("break red", num)
                        invalid = True
                        break

                elif("green" in color): 
                    color = color.replace("green", "")
                    num = int(color)
                    if(num > maxGreen): 
                        print("break green", num)
                        invalid = True
                        break

                elif("blue" in color): 
                    color = color.replace("blue", "")
                    num = int(color)
                    if(num > maxBlue): 
                        print("break blue", num)
                        invalid = True
                        break

        if(not invalid): 
            idSum += i  
            print(i, idSum)
        else: 
            invalid = False

    print(idSum)


