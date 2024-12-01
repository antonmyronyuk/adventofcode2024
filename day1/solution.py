from collections import Counter

with open("input.txt") as input_file:
    lines = input_file.read().strip().split("\n")


left, right = zip(*(map(int, line.split()) for line in lines))

# part 1
print(sum(abs(a - b) for a, b in zip(sorted(left), sorted(right))))

# part 2
right_counts = Counter(right)
print(sum(a * right_counts[a] for a in left))
