# load file
totalCalories=[]
with open("input.txt") as input:
    currentCalories = 0
    for line in input.readlines():
        if not line.strip():
            totalCalories.append(currentCalories)
            currentCalories = 0
        else:
            currentCalories += int(line.strip())
    totalCalories.append(currentCalories)
# process numbers
totalCalories.sort(reverse = True)
# output
print(totalCalories)
print(totalCalories[0] + totalCalories[1] + totalCalories[2])