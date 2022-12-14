letter_values = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("input.txt") as input:
    priority_sum = 0
    lines = input.readlines()
    while lines:
        duplicate = (set(lines.pop(0).strip()) & set(lines.pop(0).strip()) & set(lines.pop(0).strip())).pop()
        priority_sum += letter_values.index(duplicate) + 1
    print(priority_sum)
        