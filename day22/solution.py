from collections import defaultdict

with open("input.txt") as input_file:
    nums = list(map(int, input_file.read().strip().split("\n")))

n = 2000
mask = (1 << 24) - 1
def generate_secret_number(num):
    num = (num ^ num << 6) & mask
    num = (num ^ num >> 5) & mask
    num = (num ^ num << 11) & mask
    return num


def calc_part1():
    res = 0
    for num in nums:
        for _ in range(n):
            num = generate_secret_number(num)
        res += num
    return res


def calc_part2():
    diffs_to_count = defaultdict(int)
    for num in nums:
        prices = [num % 10]
        for _ in range(n):
            num = generate_secret_number(num)
            prices.append(num % 10)

        seen = set()
        for i in range(1, n - 2):
            key = tuple(prices[i + offset] - prices[i + offset - 1] for offset in range(4))
            value = prices[i + 3]
            if key not in seen:
                seen.add(key)
                diffs_to_count[key] += value

    return max(diffs_to_count.values())


print(calc_part1())
print(calc_part2())
