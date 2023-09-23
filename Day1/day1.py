maxSnackNumber1 = 0 
maxSnackNumber2 = 0 
maxSnackNumber3 = 0 

snackCounter = 0

with open("Day1\input.txt","r") as file:
    for line in file :
        print(line.strip("\n"))
        if line.strip("\n") == "":
            if snackCounter > maxSnackNumber1:
                maxSnackNumber3 = maxSnackNumber2
                maxSnackNumber2 = maxSnackNumber1
                maxSnackNumber1 = snackCounter
            elif snackCounter > maxSnackNumber2:
                maxSnackNumber3 = maxSnackNumber2
                maxSnackNumber2 = snackCounter
            elif snackCounter > maxSnackNumber3:
                maxSnackNumber3 = snackCounter
            snackCounter = 0
        else:
            value = int(line.strip("\n"))
            snackCounter += value
            


# Part1
print(maxSnackNumber1)             

#Part2
print(maxSnackNumber1 + maxSnackNumber2 + maxSnackNumber3)   
        