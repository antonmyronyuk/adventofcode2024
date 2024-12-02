with open("input.txt") as input_file:
    reports = [list(map(int, line.split())) for line in input_file.read().strip().split("\n")]


def is_safe_report(report: list[int]) -> bool:
    diffs = [a - b for a, b in zip(report, report[1:])]
    return all(1 <= diff <= 3 for diff in diffs) or all(-3 <= diff <= -1 for diff in diffs)


def is_safe_report_with_bad_level(report: list[int]) -> bool:
    cleaned_reports = [report[:i] + report[i + 1:] for i in range(len(report))]
    return any(is_safe_report(report) for report in [report] + cleaned_reports)


# part 1
print(sum(is_safe_report(report) for report in reports))

# part 2
print(sum(is_safe_report_with_bad_level(report) for report in reports))
