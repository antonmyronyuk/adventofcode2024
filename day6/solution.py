import sys
sys.setrecursionlimit(1000000)

with open("input.txt") as input_file:
    field = [list(line) for line in input_file.read().strip().split("\n")]

n, m = len(field), len(field[0])
guard_to_dirs = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
dirs = list(guard_to_dirs.values())
start_i, start_j = next((i, j) for i in range(n) for j in range(m) if field[i][j] in guard_to_dirs)
start_dir = guard_to_dirs[field[start_i][start_j]]


def walk(i, j, dir, visited=None, obstacle=None):
    visited = visited or set()
    if (i, j, dir) in visited:
        return -1  # loop

    visited.add((i, j, dir))
    ni, nj = i + dir[0], j + dir[1]
    if ni < 0 or ni >= n or nj < 0 or nj >= m:
        return len(set((i, j) for i, j, dir in visited))  # no loop

    if field[ni][nj] == "#" or (ni, nj) == obstacle:
        dir = dirs[(dirs.index(dir) + 1) % len(dirs)]
    else:
        i, j = ni, nj

    return walk(i, j, dir, visited, obstacle)


def walk_part2(i, j, dir, visited=None, obstacle=None, tried=None):
    tried = tried or set()
    visited = visited or set()
    if (i, j, dir) in visited:
        return 1  # loop

    ni, nj = i + dir[0], j + dir[1]
    if ni < 0 or ni >= n or nj < 0 or nj >= m:
        return 0  # no loop

    if not obstacle and (ni, nj) not in tried:
        with_obstacle = walk_part2(i, j, dir, visited.copy(), (ni, nj), tried.copy())
    else:
        with_obstacle = 0

    visited.add((i, j, dir))
    tried.add((i, j))
    if field[ni][nj] == "#" or (ni, nj) == obstacle:
        dir = dirs[(dirs.index(dir) + 1) % len(dirs)]
    else:
        i, j = ni, nj

    return with_obstacle + walk_part2(i, j, dir, visited, obstacle, tried)


# part 1
print(walk(start_i, start_j, start_dir))

# part 2
print(walk_part2(start_i, start_j, start_dir))
