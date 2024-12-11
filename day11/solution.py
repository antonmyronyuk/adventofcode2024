from collections import defaultdict

with open("input.txt") as input_file:
    nums = list(map(int, input_file.read().strip().split()))


def calc_stones(nums, steps):
    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1

    for _ in range(steps):
        next_counts = defaultdict(int)
        for num, count in counts.items():
            if num == 0:
                next_counts[1] += count
            elif (size :=  len(str(num))) % 2 == 0:
                div = 10**(size // 2)
                next_counts[num // div] += count
                next_counts[num % div] += count
            else:
                next_counts[num * 2024] += count
        counts = next_counts

    return sum(counts.values())


print(calc_stones(nums, 25))  # part 1
print(calc_stones(nums, 75))  # part 2
