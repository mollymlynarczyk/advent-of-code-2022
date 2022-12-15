
with open("test.txt") as input:
    worst_pairs = 0
    for line in input.readlines():
        line = line.strip()
        sections = line.split(",")
        elf1_nums = sections[0].split("-")
        elf2_nums = sections[1].split("-")
        #check first against second
        if int(elf1_nums[0]) >= int(elf2_nums[0]) and int(elf1_nums[1]) <= int(elf2_nums[1]):
            worst_pairs += 1
        elif int(elf2_nums[0]) >= int(elf1_nums[0]) and int(elf2_nums[1]) <= int(elf1_nums[1]):
            worst_pairs += 1
    print(worst_pairs)    
