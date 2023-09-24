

def firstSolution():
    stack = {"1":"SZPDLBFC","2":"NVGPHWB","3":"FWBJG","4":"GJNFLWCS","5":"WJLTPMSH","6":"BCWGFS","7":"HTPMQBW","8":"FSWT","9":"NCR"}
    with open("Day5\input.txt" ,"r") as file : 
        for line in file : 
            loopCounter = int(line.strip("\n").split(" ")[1])
            From = line.strip("\n").split(" ")[3]
            To = line.strip("\n").split(" ")[5]
            for i in range(loopCounter):
                value = stack[From][len(stack[From])-1]
                stack[From] = stack[From][:len(stack[From])-1]
                stack[To] = stack[To] + value
        for val in stack:
            print(stack[val][len(stack[val])-1],end="")
            
def secondSolution():
    stack = {"1":"SZPDLBFC","2":"NVGPHWB","3":"FWBJG","4":"GJNFLWCS","5":"WJLTPMSH","6":"BCWGFS","7":"HTPMQBW","8":"FSWT","9":"NCR"}
    with open("Day5\input.txt" ,"r") as file : 
        for line in file : 
            loopCounter = int(line.strip("\n").split(" ")[1])
            From = line.strip("\n").split(" ")[3]
            To = line.strip("\n").split(" ")[5]
            value = stack[From][len(stack[From]) - loopCounter:]
            stack[From] = stack[From][:len(stack[From]) - loopCounter]
            stack[To] = stack[To] + value
            
    for val in stack:
            print(stack[val][len(stack[val])-1],end="")
            

#Part 1 
firstSolution()
print()
#Part2
secondSolution()