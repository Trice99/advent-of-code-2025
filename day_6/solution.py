from .file_reader import FileReader
from common import SolutionRunner

def solve_problem(problem):
    nums = problem['numbers']
    op = problem['op']
    if op == '+':
        result = 0
        for n in nums:
            result += n
        return result
    if op == '*':
        result = 1
        for n in nums:
            result *= n
        return result
    raise ValueError(f'Unknown operator {op}')

def solve_all_problems(problems):
    return sum(solve_problem(p) for p in problems)

if __name__ == '__main__':
    example_reader = FileReader('example.txt')
    input_reader = FileReader('input.txt')

    example_data = example_reader.parse()
    input_data = input_reader.parse()
    example_data_rev = example_reader.parse_reversed()
    input_data_rev = input_reader.parse_reversed()

    runner = SolutionRunner(FileReader)
    runner._time_function = lambda f, d: (f(d), 0)
    
    from common import OutputFormatter
    import time
    
    start = time.time()
    ex1 = solve_all_problems(example_data)
    et1 = time.time() - start
    start = time.time()
    in1 = solve_all_problems(input_data)
    it1 = time.time() - start
    OutputFormatter.print_part(1, ex1, in1, et1, it1)
    
    start = time.time()
    ex2 = solve_all_problems(example_data_rev)
    et2 = time.time() - start
    start = time.time()
    in2 = solve_all_problems(input_data_rev)
    it2 = time.time() - start
    OutputFormatter.print_part(2, ex2, in2, et2, it2)
