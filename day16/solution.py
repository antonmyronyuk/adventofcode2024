import itertools
from heapq import heappush, heappop

with open("input.txt") as input_file:
    field = [list(line) for line in input_file.read().strip().split("\n")]

n, m = len(field), len(field[0])
start = next((i, j) for i in range(n) for j in range(m) if field[i][j] == "S")
end = next((i, j) for i in range(n) for j in range(m) if field[i][j] == "E")
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
queue = [(0, start, (0, 1), [])]  # (score, position, direction, path)
cost_map = {}  # (position, direction): score
paths_score_pairs = []


while queue:
    score, pos, dir, path  = heappop(queue)
    if (pos, dir) in cost_map and cost_map[pos, dir] < score:
        continue

    path = path + [pos]
    cost_map[pos, dir] = score

    if pos == end:
        paths_score_pairs.append((path, score))
        continue

    for di, dj in dirs:
        ni, nj = pos[0] + di, pos[1] + dj
        if field[ni][nj] in (".", "E"):
            next_score = score + (1 if dir == (di, dj) else 1001)
            heappush(queue, (next_score, (ni, nj), (di, dj), path))


min_cost = min(cost_map[end, dir] for dir in dirs if (end, dir) in cost_map)
min_cost_paths_points = set(
    itertools.chain.from_iterable(path for path, score in paths_score_pairs if score == min_cost),
)

print(min_cost)  # part 1
print(len(min_cost_paths_points))  # part 2
