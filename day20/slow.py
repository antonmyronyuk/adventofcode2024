from collections import deque

with open("input.txt") as input_file:
    field = [list(line) for line in input_file.read().strip().split("\n")]

n, m = len(field), len(field[0])
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
start = next((i, j) for i in range(n) for j in range(m) if field[i][j] == "S")
end = next((i, j) for i in range(n) for j in range(m) if field[i][j] == "E")


def calc_distance():
    visited = set()
    queue = deque([(*start, 0)])
    while queue:
        i, j, dist = queue.popleft()
        if (i, j) in visited:
            continue

        visited.add((i, j))
        if (i, j) == end:
            return dist

        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if field[ni][nj] in (".", "E"):
                queue.append((ni, nj, dist + 1))


def calc_short_ways_with_cheats(orig_dist, diff):
    res = 0
    visited = set()
    tried_cheats = set()
    queue = deque([(*start, 0, None)])
    while queue:
        i, j, dist, cheat = queue.popleft()
        if (i, j, cheat) in visited or (i, j, None) in visited:
            continue

        if dist > orig_dist - diff:
            continue

        visited.add((i, j, cheat))
        if (i, j) == end:
            res += 1
            continue

        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if field[ni][nj] in (".", "E"):
                queue.append((ni, nj, dist + 1, cheat))
            elif (
                field[ni][nj] == "#"
                and not cheat
                and 1 <= ni < n - 1
                and 1 <= nj < m - 1
                and (ni, nj) not in tried_cheats
            ):
                tried_cheats.add((ni, nj))
                queue.append((ni, nj, dist + 1, (ni, nj)))

    return res


orig_dist = calc_distance()
print(calc_short_ways_with_cheats(orig_dist, diff=100))  # part 1
