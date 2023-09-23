def firstPart():
    score = 0
    with open("Day4\input.txt","r") as file : 
        for line in file : 
            [v1,v2] = int(line.strip("\n").split(",")[0].split("-")[0]),int(line.strip("\n").split(",")[0].split("-")[1])
            [m1,m2] = int(line.strip("\n").split(",")[1].split("-")[0]),int(line.strip("\n").split(",")[1].split("-")[1])
            firstCondition = (v1 <= m1) and (v2 >= m2)
            secondCondition = (v1 >= m1) and (v2 <= m2)
            if(firstCondition or secondCondition):
                score += 1
    print(score) 
firstPart()    

def secondPart():
    score = 0
    with open("Day4\input.txt","r") as file : 
        for line in file : 
            [v1,v2] = int(line.strip("\n").split(",")[0].split("-")[0]),int(line.strip("\n").split(",")[0].split("-")[1])
            [m1,m2] = int(line.strip("\n").split(",")[1].split("-")[0]),int(line.strip("\n").split(",")[1].split("-")[1])
            firstCondition = (m1 >= v1) and (v2 >=m1)
            secondCondition = (v1 >= m1) and (m2 >=v1)
            if(firstCondition or secondCondition):
                score += 1
    print(score)
    
secondPart()
    
    



    