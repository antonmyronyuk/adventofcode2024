with open("input.txt") as input_file:
    groups = input_file.read().strip().split("\n\n")

towels = groups[0].split(", ")
patterns = groups[1].split("\n")
cache = {}


def calc_possible_combinations(pattern: str) -> int:
    if not pattern:
        return 1

    if pattern in cache:
        return cache[pattern]

    res = sum(
        calc_possible_combinations(pattern[len(towel):])
        for towel in towels
        if pattern.startswith(towel)
    )
    cache[pattern] = res
    return res


print(sum(calc_possible_combinations(pattern) > 0 for pattern in patterns))  # part 1
print(sum(calc_possible_combinations(pattern) for pattern in patterns))  # part 2
