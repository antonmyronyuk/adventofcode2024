import itertools

with open("input.txt") as input_file:
    field = [list(line) for line in input_file.read().strip().split("\n")]
    n, m = len(field), len(field[0])


def calc_part1():
    antinodes = set()
    for ai, aj in itertools.product(range(n), range(m)):
        for bi, bj in itertools.product(range(ai + 1, n), range(m)):
            if not (field[ai][aj].isalnum() and field[ai][aj] == field[bi][bj]):
                continue

            for antinode_i, antinode_j in (
                (2 * ai - bi, 2 * aj - bj),
                (2 * bi - ai, 2 * bj - aj),
            ):
                if 0 <= antinode_i < n and 0 <= antinode_j < m:
                    antinodes.add((antinode_i, antinode_j))

    return len(antinodes)


def calc_part2():
    antinodes = set()
    for ai, aj in itertools.product(range(n), range(m)):
        for bi, bj in itertools.product(range(ai + 1, n), range(m)):
            if not (field[ai][aj].isalnum() and field[ai][aj] == field[bi][bj]):
                continue

            antinodes.update(((ai, aj), (bi, bj)))
            diff_i, diff_j = ai - bi, aj - bj
            ni, nj = ai, aj
            while True:
                ni, nj = ni + diff_i, nj + diff_j
                if 0 <= ni < n and 0 <= nj < m:
                    antinodes.add((ni, nj))
                else:
                    break

            ni, nj = bi, bj
            while True:
                ni, nj = ni - diff_i, nj - diff_j
                if 0 <= ni < n and 0 <= nj < m:
                    antinodes.add((ni, nj))
                else:
                    break

    return len(antinodes)


print(calc_part1())
print(calc_part2())
