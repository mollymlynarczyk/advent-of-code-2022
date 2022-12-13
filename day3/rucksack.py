letter_values = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("input.txt") as input:
    priority_sum = 0
    for line in input.readlines():
        line = line.strip()
        first_compartment = line[0:int(len(line)/2)]
        second_compartment = line[int(len(line)/2): len(line)]
        duplicate_type = (set(first_compartment) & set(second_compartment)).pop()
        priority_sum += letter_values.index(duplicate_type) + 1
    print(priority_sum)
        