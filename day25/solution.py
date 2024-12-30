with open("input.txt") as input_file:
    patterns = []
    for pattern_raw in input_file.read().strip().split("\n\n"):
        lines = pattern_raw.split("\n")
        n, m = len(lines), len(lines[0])
        patterns.append({(i, j) for i in range(n) for j in range(m) if lines[i][j] == "#"})


res = sum(
    len(patterns[i] | patterns[j]) == len(patterns[i]) + len(patterns[j])
    for i in range(len(patterns))
    for j in range(i + 1, len(patterns))
)
print(res)
