import time
from .output_formatter import OutputFormatter


class SolutionRunner:
    def __init__(self, file_reader_class, example_file='example.txt', input_file='input.txt'):
        self.example_reader = file_reader_class(example_file)
        self.input_reader = file_reader_class(input_file)

    def _time_function(self, func, data):
        start_time = time.time()
        result = func(data)
        execution_time = time.time() - start_time
        return result, execution_time

    def run(self, part1_func, part2_func):
        example_data = self.example_reader.parse()
        input_data = self.input_reader.parse()

        example_part1, example_time1 = self._time_function(part1_func, example_data)
        input_part1, input_time1 = self._time_function(part1_func, input_data)
        OutputFormatter.print_part(1, example_part1, input_part1, example_time1, input_time1)

        example_part2, example_time2 = self._time_function(part2_func, example_data)
        input_part2, input_time2 = self._time_function(part2_func, input_data)
        OutputFormatter.print_part(2, example_part2, input_part2, example_time2, input_time2)
