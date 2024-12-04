with open("input.txt") as input_file:
    lines = input_file.read().strip().split("\n")

n, m = len(lines), len(lines[0])
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
x_dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0)]


def get_words_from_point(i, j):
    for (di, dj) in dirs:
        word = ""
        for k in range(4):
            ni, nj = i + k * di, j + k * dj
            if 0 <= ni < n and 0 <= nj < m:
                word += lines[ni][nj]
            else:
                break

        if len(word) == 4:
            yield word


def get_x_word_from_point(i, j):
    return "".join(lines[i + di][j + dj] for di, dj in x_dirs)


res_part1 = sum(
    sum(word == "XMAS" for word in get_words_from_point(i, j))
    for i in range(n)
    for j in range(m)
)
res_part2 = sum(
    get_x_word_from_point(i, j) in ("SMSMA", "MSMSA", "SSMMA", "MMSSA")
    for i in range(1, n - 1)
    for j in range(1, m - 1)
)
print(res_part1)
print(res_part2)
