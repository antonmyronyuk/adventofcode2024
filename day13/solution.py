import re

with open("input.txt") as input_file:
    groups = input_file.read().strip().split("\n\n")


def calc_tokens(offset):
    """
    ax * a + bx * b = px
    ay * a + by * b = py
    b = (px - ax * a) / bx
    ay * a + by * (px - ax * a) / bx = py
    bx * ay * a + by * px - by * ax * a = py * bx
    bx * ay * a - by * ax * a = py * bx - by * px
    a * (bx * ay - by * ax) = py * bx - by * px
    a = (py * bx - by * px) / (bx * ay - by * ax)
    """
    res = 0
    for group in groups:
        ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", group))
        px, py = px + offset, py + offset
        a = (py * bx - by * px) / (bx * ay - by * ax)
        b = (px - ax * a) / bx
        if a == int(a) and b == int(b):
            res += 3 * int(a) + int(b)

    return res


print(calc_tokens(offset=0))  # part 1
print(calc_tokens(offset=10000000000000))  # part 2
