from .file_reader import FileReader
from common import OutputFormatter
import time

def solve_part1(data):
    return count_all_paths(data, 'you', 'out')

def solve_part2(data, required):
    return count_paths_with_required(data, 'svr', 'out', required)

def count_all_paths(graph, start, end):
    def dfs(current, visited):
        if current == end:
            return 1
        
        if current in visited or current not in graph:
            return 0
        
        visited.add(current)
        total = sum(dfs(neighbor, visited) for neighbor in graph[current])
        visited.remove(current)
        
        return total
    
    return dfs(start, set())

def count_paths_with_required(graph, start, end, required_nodes):
    required_list = sorted(required_nodes)
    required_mask = (1 << len(required_list)) - 1
    node_to_bit = {node: (1 << i) for i, node in enumerate(required_list)}
    cache = {}
    
    def dfs(current, visited, seen_mask):
        if current == end:
            return 1 if seen_mask == required_mask else 0
        
        if current in visited:
            return 0
        
        cache_key = (current, seen_mask)
        if cache_key in cache:
            return cache[cache_key]
        
        if current not in graph:
            cache[cache_key] = 0
            return 0
        
        visited.add(current)
        updated_mask = seen_mask | node_to_bit.get(current, 0)
        total = sum(dfs(neighbor, visited, updated_mask) for neighbor in graph[current])
        visited.remove(current)
        
        cache[cache_key] = total
        return total
    
    initial_mask = node_to_bit.get(start, 0)
    return dfs(start, set(), initial_mask)

if __name__ == '__main__':
    example_part1_reader = FileReader('example_part1.txt')
    example_part2_reader = FileReader('example_part2.txt')
    input_reader = FileReader('input.txt')

    example_data_part1 = example_part1_reader.parse()
    example_data_part2 = example_part2_reader.parse()
    input_data = input_reader.parse()

    start = time.time()
    example_part1 = solve_part1(example_data_part1)
    example_time1 = time.time() - start
    start = time.time()
    input_part1 = solve_part1(input_data)
    input_time1 = time.time() - start
    OutputFormatter.print_part(1, example_part1, input_part1, example_time1, input_time1)

    required = {'dac', 'fft'}
    start = time.time()
    example_part2 = solve_part2(example_data_part2, required)
    example_time2 = time.time() - start
    start = time.time()
    input_part2 = solve_part2(input_data, required)
    input_time2 = time.time() - start
    OutputFormatter.print_part(2, example_part2, input_part2, example_time2, input_time2)
