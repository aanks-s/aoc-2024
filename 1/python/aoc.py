from collections import Counter

with open('input.txt', 'r') as fd:
    data = [line.strip().split() for line in fd]

left = sorted(int(row[0]) for row in data)
right = sorted(int(row[-1]) for row in data)

part_1 = sum(abs(l - r) for l, r in zip(left, right))
print(part_1)

counts_right = Counter(right)
part_2 = sum(number * counts_right[number] for number in left)
print(part_2)
