from collections import defaultdict

with open("input.txt") as input_file:
    rules_raw, updates_raw = input_file.read().strip().split("\n\n")

updates = [list(map(int, row.split(","))) for row in updates_raw.split("\n")]
rules_after = defaultdict(set)
for row in rules_raw.split("\n"):
    page_before, page_after = list(map(int, row.split("|")))
    rules_after[page_after].add(page_before)


def bubble_sort(pages: list[int]) -> list[int]:
    for i in range(len(pages) - 1):
        for j in range(i + 1, len(pages)):
            if pages[j] in rules_after[pages[i]]:
                pages[i], pages[j] = pages[j], pages[i]

    return pages


res_part1 = res_part2 = 0
for pages in updates:
    sorted_pages = bubble_sort(pages.copy())
    middle_number = sorted_pages[len(sorted_pages) // 2]
    if pages == sorted_pages:
        res_part1 += middle_number
    else:
        res_part2 += middle_number

print(res_part1)
print(res_part2)
