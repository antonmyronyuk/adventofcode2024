from collections import deque

with open("input.txt") as input_file:
    field = [list(line) for line in input_file.read().strip().split("\n")]

n, m = len(field), len(field[0])
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
start = next((i, j) for i in range(n) for j in range(m) if field[i][j] == "S")
end = next((i, j) for i in range(n) for j in range(m) if field[i][j] == "E")

# calc all the distances from start
dist_map = [[float("inf")] * m for _ in range(n)]
queue = deque([(*start, 0)])
while queue:
    i, j, dist = queue.popleft()
    if dist_map[i][j] <= dist:
        continue

    dist_map[i][j] = dist

    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if field[ni][nj] in (".", "E"):
            queue.append((ni, nj, dist + 1))


def calc_short_ways_with_cheats(diff, max_cheat_size):
    res = 0
    for si in range(1, n - 1):
        for sj in range(1, m - 1):
            if field[si][sj] == "#":
                continue
            for ei in range(max(1, si - max_cheat_size - 1), min(n - 1, si + max_cheat_size + 2)):
                for ej in range(max(1, sj - max_cheat_size - 1), min(m - 1, sj + max_cheat_size + 2)):
                    if field[ei][ej] == "#":
                        continue
                    cheat_size = abs(si - ei) + abs(sj - ej) - 1
                    if cheat_size > max_cheat_size or cheat_size <= 0:
                        continue

                    if dist_map[ei][ej] - dist_map[si][sj] - cheat_size - 1 >= diff:
                        res += 1

    return res


print(calc_short_ways_with_cheats(diff=100, max_cheat_size=1))  # part 1
print(calc_short_ways_with_cheats(diff=100, max_cheat_size=19))  # part 2
