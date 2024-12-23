import itertools

with open("input.txt") as input_file:
    edges = set(frozenset(row.split("-")) for row in input_file.read().strip().split("\n"))

vertices = list(set(itertools.chain.from_iterable(edges)))
n = len(vertices)

def is_connected(a, b):
    return {a, b} in edges


def calc_part1():
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if not is_connected(vertices[i], vertices[j]):
                continue
            for k in range(j + 1, n):
                if is_connected(vertices[j], vertices[k]) and is_connected(vertices[k], vertices[i]):
                    codes = [vertices[index] for index in (i, j, k)]
                    res += any(code.startswith("t") for code in codes)
    return res


def calc_part2():
    connected_components = set(edges)
    while len(connected_components) > 1:
        next_connected_components = set()
        for cc in connected_components:
            for i in range(n):
                new_code = vertices[i]
                if new_code not in cc and all(is_connected(new_code, code) for code in cc):
                    next_connected_components.add(frozenset([*cc, new_code]))

        connected_components = next_connected_components

    return ",".join(sorted(connected_components.pop()))


print(calc_part1())
print(calc_part2())
