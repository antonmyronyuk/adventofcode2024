from collections import deque

with open("input.txt") as input_file:
    points = [
        tuple(map(int, line.split(",")))
        for line in input_file.read().strip().split("\n")
    ]

for k in range(len(points)):
    corrupted = set(points[:k])
    n, m = 71, 71
    visited = set()
    queue = deque([(0, 0, 0)])
    reached_end = False
    while queue:
        i, j, dist = queue.popleft()
        if (i, j) in visited:
            continue

        visited.add((i, j))
        if i == n - 1 and j == m - 1:
            reached_end = True
            break

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and (nj, ni) not in corrupted:
                queue.append((ni, nj, dist + 1))

    if reached_end and k == 1024:
        print("part 1", dist)

    if not reached_end:
        print("part 2", points[k - 1])
        break
