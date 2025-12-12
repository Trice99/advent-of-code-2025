from .file_reader import FileReader
from common import SolutionRunner

def is_fresh(n, ranges):
    return any(start <= n <= end for start, end in ranges)

def count_fresh(data):
    ranges, ids = data
    return sum(1 for n in ids if is_fresh(n, ranges))

def count_total_fresh(data):
    ranges, _ = data
    sorted_ranges = sorted(ranges)
    merged = []
    for start, end in sorted_ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return sum(end - start + 1 for start, end in merged)

if __name__ == '__main__':
    runner = SolutionRunner(FileReader)
    runner.run(count_fresh, count_total_fresh)