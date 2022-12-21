with open("input.txt") as input:
    line = input.readlines()[0]
    last_four = []
    marker_count = 14
    for i in range(len(line)):
        char = line[i]
        last_four.append(char)
        if len(last_four) == (marker_count + 1):
            last_four.pop(0)
        if len(last_four) == marker_count and len(set(last_four)) == marker_count:
            print("First marker at " + str(i + 1))
            break
            