with open('input.txt', 'r') as fd:
    data = [[int(i) for i in line.strip().split()] for line in fd]

part_1 = 0
final_safe = 0


def safe_part_1(sublist):
    increasing = all(sublist[i + 1] > sublist[i] for i in range(len(sublist) - 1))
    decreasing = all(sublist[i + 1] < sublist[i] for i in range(len(sublist) - 1))
    validated_diff = all(1 <= abs(sublist[i + 1] - sublist[i]) <= 3 for i in range(len(sublist) - 1))

    return (increasing or decreasing) and validated_diff


for sublist in data:
    if safe_part_1(sublist):
        part_1 += 1
        final_safe += 1
    # Add part_2 rule
    else:
        is_safe = False
        for i in range(len(sublist)):
            new_sublist = sublist[:i] + sublist[i + 1:]
            if safe_part_1(new_sublist):
                final_safe += 1
                is_safe = True
                break

print(part_1)
print(final_safe)
