from .file_reader import FileReader
from collections import defaultdict
from common import SolutionRunner

def get_start_position(grid):
    return 0, grid[0].index('S')

def get_next_positions(grid, row, col):
    next_row = row + 1
    if next_row >= len(grid):
        return []
    
    cell = grid[next_row][col]
    if cell in ('.', 'S'):
        return [(next_row, col)]
    
    if cell == '^':
        positions = []
        if col > 0:
            positions.append((next_row, col - 1))
        if col < len(grid[0]) - 1:
            positions.append((next_row, col + 1))
        return positions
    
    return [(next_row, col)]

def simulate_splits(grid):
    stack = [get_start_position(grid)]
    visited = set()
    split_count = 0

    while stack:
        row, col = stack.pop()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        
        if row + 1 < len(grid) and grid[row + 1][col] == '^':
            split_count += 1
        
        stack.extend(get_next_positions(grid, row, col))
    
    return split_count

def simulate_timelines(grid):
    paths = defaultdict(int)
    paths[get_start_position(grid)] = 1
    
    for _ in range(len(grid) - 1):
        new_paths = defaultdict(int)
        for (r, c), cnt in paths.items():
            for nr, nc in get_next_positions(grid, r, c):
                new_paths[(nr, nc)] += cnt
        paths = new_paths
    
    return sum(paths.values())

if __name__ == '__main__':
    runner = SolutionRunner(FileReader)
    runner.run(simulate_splits, simulate_timelines)
