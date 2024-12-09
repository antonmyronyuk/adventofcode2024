with open("input.txt") as input_file:
    data = input_file.read().strip()


def calc_part1():
    memory = []
    for i, size in enumerate(data):
        memory += [i // 2 if i % 2 == 0 else -1] * int(size)

    i, j = 0, len(memory) - 1
    while i < j:
        if memory[i] != -1:
            i += 1
        elif memory[j] == -1:
            j -= 1
        else:
            memory[i], memory[j] = memory[j], memory[i]
            i, j = i + 1, j - 1

    return sum(i * file_id for i, file_id in enumerate(memory[:j + 1]))


def calc_part2():
    offset = 0
    free_blocks = {}
    file_blocks = {}
    for i, size in enumerate(data):
        block_size = int(size)
        block_id = i // 2 if i % 2 == 0 else -1
        offset += block_size
        if block_id == -1 and block_size > 0:
            free_blocks[offset - 1] = block_size
        elif block_id >= 0:
            file_blocks[offset - 1] = (block_id, block_size)

    j = offset - 1
    while j >= 0:
        if j in file_blocks:
            block_id, block_size = file_blocks[j]
            for free_block_end, free_block_size in free_blocks.items():
                if j > free_block_end and free_block_size >= block_size:
                    file_blocks.pop(j)
                    diff_size = free_block_size - block_size
                    file_blocks[free_block_end - diff_size] = (block_id, block_size)
                    if diff_size == 0:
                        free_blocks.pop(free_block_end)
                    else:
                        free_blocks[free_block_end] = diff_size
                    break
            if j in file_blocks:  # not moved
                j -= 1
        else:
            j -= 1

    checksum = 0
    for block_end, (block_id, block_size) in file_blocks.items():
        for k in range(block_end - block_size + 1, block_end + 1):
            checksum += block_id * k

    return checksum


print(calc_part1())
print(calc_part2())
