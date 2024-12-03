import re

with open("input.txt") as input_file:
    data = input_file.read()

res_part1 = 0
for instruction in re.findall(r"mul\(\d+,\d+\)", data):
    a, b = list(map(int,  re.findall(r"\d+", instruction)))
    res_part1 += a * b

res_part2 = 0
ignore_instruction = False
for instruction in re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", data):
    if instruction == "don't()":
        ignore_instruction = True
    elif instruction == "do()":
        ignore_instruction = False
    elif not ignore_instruction:
        a, b = list(map(int,  re.findall(r"\d+", instruction)))
        res_part2 += a * b

print(res_part1)
print(res_part2)
