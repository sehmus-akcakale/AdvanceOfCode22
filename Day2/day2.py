# A -- Rock
# B -- Paper
# C -- Scissors

# X -- Rock
# Y -- Paper
# Z -- Scissors

# 1 for Rock, 2 for Paper, and 3 for Scissors
# Winning - 6 , Losing - 0 , Tie - 3

# X -- Lose , Y -- Draw , Z -- Win 
def solution1():
    score = 0 
    points = {"X":1,"Y":2,"Z":3,"winning":6,"losing":0,"tie":3}
    with open("Day2\input.txt","r") as file : 
        for line in file : 
            [enemy , us] = line.strip("\n").split(" ")
            score += points[us]
            if us == "X":
                if enemy == "A":
                    score += points["tie"]
                elif enemy == "B":
                    score += points["losing"]
                else:
                    score += points["winning"]
            
            elif us == "Y":
                if enemy == "A":
                    score += points["winning"]
                elif enemy == "B":
                    score += points["tie"]
                else:
                    score += points["losing"]
            
            elif us == "Z":
                if enemy == "A":
                    score += points["losing"]
                elif enemy == "B":
                    score += points["winning"]
                else:
                    score += points["tie"]
    return score
print(solution1())


# X - Lose , Y - Draw , Z - Win

# A -- Rock
# B -- Paper
# C -- Scissors

# X -- Rock
# Y -- Paper
# Z -- Scissors

def solution2():
    
    score = 0 
    points = {"X":1,"Y":2,"Z":3,"winning":6,"losing":0,"tie":3}
    
    with open("Day2\input.txt","r") as file : 
        for line in file : 
            
            [enemy,gameSituation] = line.strip("\n").split(" ")
            
            if(gameSituation == "X"):
                score += points["losing"]
                if (enemy == "A"):
                    score += points["Z"]
                elif (enemy == "B"):
                    score+= points["X"]
                else:
                    score += points["Y"]
                    
            elif (gameSituation == "Y"):
                score += points["tie"]
                if(enemy == "A"):
                    score += points["X"]
                elif (enemy == "B"):
                    score += points["Y"]
                else:
                    score += points["Z"]
                    
            else:
                score += points["winning"]
                if(enemy == "A"):
                    score += points["Y"]
                elif (enemy == "B"):
                    score += points["Z"]
                else:
                    score += points["X"]
                    
    return score
        
print(solution2())