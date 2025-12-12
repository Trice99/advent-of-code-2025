from .file_reader import FileReader
from common import SolutionRunner

def max_joltage_for_bank(bank):
    best = 0
    n = len(bank)

    for i in range(n):
        for j in range(i + 1, n):
            val = int(bank[i] + bank[j])
            if val > best:
                best = val

    return best

def max_joltage_for_bank_k(bank, k):
    to_remove = len(bank) - k
    stack = []

    for digit in bank:
        while to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    return int(''.join(stack[:k]))

def solve_part1(data):
    return sum(max_joltage_for_bank(b) for b in data)

def solve_part2(data):
    return sum(max_joltage_for_bank_k(b, 12) for b in data)

if __name__ == '__main__':
    runner = SolutionRunner(FileReader)
    runner.run(solve_part1, solve_part2)
