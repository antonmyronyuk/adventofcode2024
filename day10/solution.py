from collections import deque

with open("input.txt") as input_file:
    field = [list(map(int, line)) for line in input_file.read().strip().split("\n")]
    n, m = len(field), len(field[0])


def calc_trailhead_score(i, j, unique=True):
    if field[i][j] != 0:
        return 0

    count = 0
    visited = set()
    queue = deque([(i, j)])

    while queue:
        i, j = queue.popleft()
        if unique and (i, j) in visited:
            continue

        visited.add((i, j))
        if field[i][j] == 9:
            count += 1
            continue

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and field[ni][nj] == field[i][j] + 1:
                queue.append((ni, nj))

    return count


print(sum(calc_trailhead_score(i, j, unique=True) for i in range(n) for j in range(m)))  # part 1
print(sum(calc_trailhead_score(i, j, unique=False) for i in range(n) for j in range(m)))  # part 2
