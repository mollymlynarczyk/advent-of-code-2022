
with open("input.txt") as input:
    worst_pairs = 0
    for line in input.readlines():
        line = line.strip()
        sections = line.split(",")
        elf1_nums = sections[0].split("-")
        elf2_nums = sections[1].split("-")
        if (not int(elf1_nums[1]) < int(elf2_nums[0])) and (not int(elf2_nums[1]) < int(elf1_nums[0])):
            print(line + " Overlap")
            worst_pairs += 1
    print(worst_pairs) 