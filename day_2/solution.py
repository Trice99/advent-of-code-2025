from .file_reader import FileReader
from common import SolutionRunner

def has_repeating_pattern(s, pattern_length):
    if len(s) % pattern_length != 0:
        return False
    pattern = s[:pattern_length]
    return pattern * (len(s) // pattern_length) == s

def is_invalid_id(n, part1=False):
    s = str(n)
    length = len(s)
    
    if part1:
        return length % 2 == 0 and has_repeating_pattern(s, length // 2)
    
    return any(has_repeating_pattern(s, k) for k in range(1, length // 2 + 1))

def sum_invalid_ids_part1(ranges):
    return sum(
        n for start, end in ranges 
        for n in range(start, end + 1) 
        if is_invalid_id(n, part1=True)
    )

def sum_invalid_ids(ranges):
    return sum(
        n for start, end in ranges 
        for n in range(start, end + 1) 
        if is_invalid_id(n, part1=False)
    )

if __name__ == '__main__':
    runner = SolutionRunner(FileReader)
    runner.run(sum_invalid_ids_part1, sum_invalid_ids)