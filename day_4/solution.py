from .file_reader import FileReader
from common import SolutionRunner

DIRS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

def count_adjacent_at(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    total = 0

    for dr, dc in DIRS:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == '@':
                total += 1
    return total

def find_accessible_positions(grid):
    rows = len(grid)
    cols = len(grid[0])
    acc = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                if count_adjacent_at(grid, r, c) < 4:
                    acc.append((r, c))
    return acc

def count_accessible_rolls(grid):
    return len(find_accessible_positions(grid))

def simulate_removals(grid):
    grid = [row[:] for row in grid]
    total_removed = 0

    while True:
        accessible = find_accessible_positions(grid)
        if not accessible:
            break

        for r, c in accessible:
            grid[r][c] = '.'

        total_removed += len(accessible)

    return total_removed

if __name__ == '__main__':
    runner = SolutionRunner(FileReader)
    runner.run(count_accessible_rolls, simulate_removals)
