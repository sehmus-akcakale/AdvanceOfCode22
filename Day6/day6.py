inp = ""
with open("Day6\input.txt","r") as file:
    inp = file.read()
    
    
def generalSolution(inp : str , distinctCharacterCount : int):
    count = 0
    while(count + distinctCharacterCount < len(inp)):
        subStr = inp[count : count + distinctCharacterCount]
        condition = True
        for char in subStr:
            if(subStr.count(char) != 1):
                condition = False
                break
        if(condition):
            return count + distinctCharacterCount
        count = count + 1
        

#Part1
print(generalSolution(inp,4))

#Part2
print(generalSolution(inp,14))