from collections import Counter

with open("input.txt") as input_file:
    codes = input_file.read().strip().split("\n")

num_keypad_button_to_position = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "#": (3, 0),
    "0": (3, 1),
    "A": (3, 2),
}
dir_keypad_button_to_position = {
    "#": (0, 0),
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}

def get_num_path(start, finish):
    sy, sx = num_keypad_button_to_position[start]
    fy, fx = num_keypad_button_to_position[finish]
    dy, dx = fy - sy, fx - sx
    dy_move = "v" if dy > 0 else "^"
    dx_move = ">" if dx > 0 else "<"
    if dy < 0:
        if (start in "0A" and finish in "147") or dx > 0:
            return dy_move * abs(dy) + dx_move * abs(dx)
        else:
            return dx_move * abs(dx) + dy_move * abs(dy)
    else:
        if (start in "147" and finish in "0A") or dx < 0:
            return dx_move * abs(dx) + dy_move * abs(dy)
        else:
            return dy_move * abs(dy) + dx_move * abs(dx)


def get_dir_path(start, finish):
    sy, sx = dir_keypad_button_to_position[start]
    fy, fx = dir_keypad_button_to_position[finish]
    dy, dx = fy - sy, fx - sx
    dy_move = "v" if dy > 0 else "^"
    dx_move = ">" if dx > 0 else "<"
    if dy < 0:
        if (start in "<" and finish in "^A") or dx < 0:
            return dx_move * abs(dx) + dy_move * abs(dy)
        else:
            return dy_move * abs(dy) + dx_move * abs(dx)
    else:
        if (start in "^A" and finish in "<") or dx > 0:
            return dy_move * abs(dy) + dx_move * abs(dx)
        else:
            return dx_move * abs(dx) + dy_move * abs(dy)


def path_to_pairs(path):
    return list(zip(path, path[1:]))


def get_outer_path_length(code, num_dir_keypads):
    next_path = ""
    for s, f in path_to_pairs("A" + code):
        next_path += get_num_path(s, f) + "A"

    pair_counts = Counter(path_to_pairs("A" + next_path))
    for _ in range(num_dir_keypads):
        next_counts = Counter()
        for (s, f), count in pair_counts.items():
            next_pairs = path_to_pairs("A" + get_dir_path(s, f) + "A")
            next_counts.update(dict.fromkeys(next_pairs, count))
        pair_counts = next_counts

    return sum(pair_counts.values())


def calc_total_complexity(num_dir_keypads):
    return sum(int(code[:-1]) * get_outer_path_length(code, num_dir_keypads) for code in codes)


print(calc_total_complexity(2))  # part 1
print(calc_total_complexity(25))  # part 2
