import math

with open("input.txt") as input:
    lines = input.readlines()
    #find the number of stacks
    for line in lines:
        if line[1] == '1':
            num_stacks = math.floor(len(line)/4)
            break
    
    stacks = [[] for i in range(num_stacks)]
    original_position = True
    for line in lines:
        if line[0] == '\n' or line[1] == '1':
            original_position = False
        elif original_position:
            #process original arrangement
            for x in range(0, num_stacks):
                pos = 4*x+1
                if not line[pos] == ' ':
                    stacks[x].insert(0, line[pos])
        else:
            #process the directions
            directions = line.split()
            crates = int(directions[1])
            from_stack = int(directions[3]) - 1
            to_stack = int(directions[5]) - 1
            crates_to_move = []
            #multiple crates moved at a time
            for i in range(crates):
                crates_to_move.insert(0, stacks[from_stack].pop())
            stacks[to_stack] = stacks[to_stack] + crates_to_move
    result = ""
    for i in range(num_stacks):
        result = result + stacks[i].pop()
    print(result)

            
    