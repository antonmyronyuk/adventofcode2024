from collections import defaultdict, deque

with open("input.txt") as input_file:
    field = [list(line) for line in input_file.read().strip().split("\n")]
    n, m = len(field), len(field[0])

visited = set()
regions = []

for start_i in range(n):
    for start_j in range(m):
        if (start_i, start_j) not in visited:
            regions.append([])

        queue = deque([(start_i, start_j)])
        while queue:
            i, j = queue.pop()
            if (i, j) in visited:
                continue

            regions[-1].append((i, j))
            visited.add((i, j))

            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and field[ni][nj] == field[i][j]:
                    queue.append((ni, nj))


def get_border_edges(region):
    edges_count = defaultdict(int)
    for i, j in region:
        edges_count["W", i, j] += 1
        edges_count["W", i, j + 1] += 1
        edges_count["H", i, j] += 1
        edges_count["H", i + 1, j] += 1

    return [edge for edge, count in edges_count.items() if count == 1]


def calc_sides(region):
    border_edges = set(get_border_edges(region))
    turns = 1
    cur = sorted(border_edges)[0]
    border_edges.remove(cur)
    while border_edges:
        moved = False
        side, i, j = cur

        # no turn
        if side == "H":
            for offset_j in (1, -1):
                if (
                    (side, i, j + offset_j) in border_edges
                    and ("W", i, j + (offset_j > 0)) not in border_edges
                    and ("W", i - 1, j + (offset_j > 0)) not in border_edges
                ):
                    cur = (side, i, j + offset_j)
                    border_edges.remove(cur)
                    moved = True
                    break
        else:
            for offset_i in (1, -1):
                if (
                    (side, i + offset_i, j) in border_edges
                    and ("H", i + (offset_i > 0), j) not in border_edges
                    and ("H", i + (offset_i > 0), j - 1) not in border_edges
                ):
                    cur = (side, i + offset_i, j)
                    border_edges.remove(cur)
                    moved = True
                    break

        if moved:
            continue

        # turn
        if side == "H":
            for offset_i, offset_j in [(-1, 0), (0, 0), (-1, 1), (0, 1)]:
                if ("W", i + offset_i, j + offset_j) in border_edges:
                    cur = ("W", i + offset_i, j + offset_j)
                    border_edges.remove(cur)
                    turns += 1
                    moved = True
                    break
        else:
            for offset_i, offset_j in [(0, -1), (0, 0), (1, -1), (1, 0)]:
                if ("H", i + offset_i, j + offset_j) in border_edges:
                    cur = ("H", i + offset_i, j + offset_j)
                    border_edges.remove(cur)
                    turns += 1
                    moved = True
                    break

        # inner figures
        if not moved:
            cur = sorted(border_edges)[0]
            border_edges.remove(cur)
            turns += 1

    return turns


print(sum(len(region) * len(get_border_edges(region)) for region in regions))  # part 1
print(sum(len(region) * calc_sides(region) for region in regions))  # part 2
