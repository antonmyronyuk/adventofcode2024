with open("input.txt") as input_file:
    lines = input_file.read().strip().split("\n")


def is_possible_equation(res, nums, cur, with_concat=False):
    if not nums:
        return res == cur

    return (
        is_possible_equation(res, nums[1:], cur + nums[0], with_concat)
        or is_possible_equation(res, nums[1:], cur * nums[0], with_concat)
        or (with_concat and is_possible_equation(res, nums[1:], int(f"{cur}{nums[0]}"), with_concat))
    )


def calc_possible_equations(with_concat=False):
    total = 0
    for line in lines:
        res_raw, nums_raw = line.split(": ")
        res, nums = int(res_raw), list(map(int, nums_raw.split(" ")))
        if is_possible_equation(res, nums[1:], nums[0], with_concat):
            total += res

    return total


print(calc_possible_equations(with_concat=False))  # part 1
print(calc_possible_equations(with_concat=True))  # part 2
