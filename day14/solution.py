import re
from collections import deque

with open("input.txt") as input_file:
    robots = input_file.read().strip().split("\n")
    n, m = 103, 101


def move(moves):
    field = [[0] * m for _ in range(n)]
    for robot in robots:
        py, px, vy, vx = map(int, re.findall(r"-?\d+", robot))
        field[(px + vx * moves) % n][(py + vy * moves) % m] += 1

    return field


def cacl_safety_factor(field):
    res = 1
    for i_start, i_end in ((0, n // 2), (n // 2 + 1, n)):
        for j_start, j_end in ((0, m // 2), (m // 2 + 1, m)):
            res *= sum(field[i][j] for i in range(i_start, i_end) for j in range(j_start, j_end))

    return res


def get_max_connected_area(field):
    positions = set((i, j) for i in range(n) for j in range(m) if field[i][j] > 0)
    start = min(positions)
    positions.remove(start)
    visited = set()
    queue = deque([start])
    max_connected_area = 0
    while queue:

        i, j = queue.popleft()
        if (i, j) in visited:
            continue

        visited.add((i, j))
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if (ni, nj) in positions:
                positions.remove((ni, nj))
                queue.append((ni, nj))

        if not queue and positions:
            max_connected_area = max(max_connected_area, len(visited))
            visited.clear()
            start = min(positions)
            positions.remove(start)
            queue.append(start)

    return max_connected_area


print(cacl_safety_factor(move(100)))  # part 1

# part 2
target_moves = 0
max_area = 0
for k in range(n * m):
    area = get_max_connected_area(move(k))
    if area > max_area:
        max_area = area
        target_moves = k

print(target_moves)
