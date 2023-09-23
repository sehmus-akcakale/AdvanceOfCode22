
def firstSolution():
    score = 0
    with open("Day3\input.txt","r") as file : 
        for line in file : 
            leftSubStr = line[:len(line) // 2]
            rightSubStr = line[len(line) // 2 :]
            isFind = False
            for chr1 in leftSubStr:
                for chr2 in rightSubStr:
                    if chr1 == chr2:
                        isFind = True
                        if(chr1.islower()):
                            score += ord(chr1) - 96
                        else:
                            score += ord(chr1) - 38
                        break
                if(isFind):
                    break
    return score

print(firstSolution())

def secondSolution():
    score = 0
    counter = 0 
    rucksacks = ["","",""]
    with open("Day3\input.txt","r") as file : 
        for line in file : 
            rucksacks[counter] = line.strip("\n")
            counter = counter + 1 
            if(counter == 3):
                counter = 0
                for char in rucksacks[0]:
                    condition = (char in rucksacks[1]) and (char in rucksacks[2])
                    if condition:
                        if(char.islower()):
                            score += ord(char) - 96
                        else:
                            score += ord(char) - 38
                        break

            
    return score
print(secondSolution())      
 
            