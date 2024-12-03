import re

with open('input.txt', 'r') as fd:
    data = fd.read()

regex = r'mul\((\d{1,3}),(\d{1,3})\)'
total_sum_part1 = sum(int(x) * int(y) for x, y in re.findall(regex, data))
print(total_sum_part1)

regex_do = r'do\(\)'
regex_dont = r'don\'t\(\)'
enabled = True
mul_list = []
combined_regex = f'{regex}|{regex_do}|{regex_dont}'
for match in re.finditer(combined_regex, data):
    instruction = match.group(0)
    if re.fullmatch(regex_do, instruction):
        enabled = True
    elif re.fullmatch(regex_dont, instruction):
        enabled = False
    elif match := re.fullmatch(regex, instruction):
        if enabled:
            mul_list.append(match.groups())

total_sum_part2 = sum(int(x) * int(y) for x, y in mul_list)
print(total_sum_part2)
