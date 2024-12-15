import itertools

with open("input.txt") as input_file:
    field_raw, moves_raw = input_file.read().strip().split("\n\n")

moves = moves_raw.replace("\n", "")
move_to_dir = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def get_closest_empty_position(field, i, j, di, dj):
    while True:
        ni, nj = i + di, j + dj
        if field[ni][nj] == ".":
            return ni, nj
        if field[ni][nj] == "#":
            return None
        i, j = ni, nj


def get_positions_to_move(field, i, j, di, dj):
    ni, nj = i + di, j + dj
    positions = {(ni, nj), (ni, (nj + 1) if field[ni][nj] == "[" else (nj - 1))}
    current_layer = positions.copy()
    while current_layer:
        next_layer = set()
        for i, j in current_layer:
            ni, nj = i + di, j + dj
            if field[ni][nj] == "#":
                return None
            if field[ni][nj] == ".":
                continue
            if field[ni][nj] == "[":
                next_layer.update([(ni, nj), (ni, nj + 1)])
            elif field[ni][nj] == "]":
                next_layer.update([(ni, nj), (ni, nj - 1)])
        positions.update(next_layer)
        current_layer = next_layer

    return positions


def calc_part1():
    field = [list(line) for line in field_raw.split("\n")]
    n, m = len(field), len(field[0])
    i, j = next((i, j) for i in range(n) for j in range(m) if field[i][j] == "@")
    for move in moves:
        di, dj = move_to_dir[move]
        ni, nj = i + di, j + dj
        if field[ni][nj] == "#":
            continue
        if field[ni][nj] == ".":
            field[i][j], field[ni][nj] = field[ni][nj], field[i][j]
        else:
            closest_empty_pos = get_closest_empty_position(field, i, j, di, dj)
            if not closest_empty_pos:
                continue
            ei, ej = closest_empty_pos
            field[i][j], field[ni][nj], field[ei][ej] = field[ei][ej], field[i][j], field[ni][nj]
        i, j = ni, nj

    return sum(100 * i + j for i in range(n) for j in range(m) if field[i][j] == "O")


def calc_part2():
    transform_map = {"#": ["#", "#"], "O": ["[", "]"], ".": [".", "."], "@": ["@", "."]}
    field = [
        list(itertools.chain.from_iterable(transform_map[char] for char in line))
        for line in field_raw.split("\n")
    ]
    n, m = len(field), len(field[0])
    i, j = next((i, j) for i in range(n) for j in range(m) if field[i][j] == "@")
    for move in moves:
        di, dj = move_to_dir[move]
        ni, nj = i + di, j + dj
        if field[ni][nj] == "#":
            continue
        if field[ni][nj] == ".":
            field[i][j], field[ni][nj] = field[ni][nj], field[i][j]
        else:
            if di == 0:
                closest_empty_pos = get_closest_empty_position(field, i, j, di, dj)
                if not closest_empty_pos:
                    continue
                ei, ej = closest_empty_pos
                field[i][nj:ej + dj:dj] = field[i][j:ej:dj]
                field[i][j] = "."
            else:
                positions_to_move = get_positions_to_move(field, i, j, di, dj)
                if not positions_to_move:
                    continue
                for pi, pj in sorted(positions_to_move, reverse=di > 0):
                    field[pi + di][pj + dj], field[pi][pj] = field[pi][pj], field[pi + di][pj + dj]
                field[i][j], field[ni][nj] =  field[ni][nj], field[i][j]
        i, j = ni, nj

    return sum(100 * i + j for i in range(n) for j in range(m) if field[i][j] == "[")


print(calc_part1())
print(calc_part2())
