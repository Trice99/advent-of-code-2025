from .file_reader import FileReader
from collections import deque
from multiprocessing import Pool, cpu_count
from common import SolutionRunner

def solve_machines_part1(machines):
    total = 0
    for machine in machines:
        lights_str = ''.join('#' if bit == 1 else '.' for bit in machine["target"])
        n = len(lights_str)
        
        start_state = 0
        for i, char in enumerate(lights_str):
            if char == "#":
                start_state |= 1 << i
        
        if start_state == 0:
            continue
        
        buttons = []
        for btn in machine["buttons"]:
            mask = 0
            for idx in btn:
                if 0 <= idx < n:
                    mask |= 1 << idx
            buttons.append(mask)
        
        visited = {start_state}
        queue = deque([start_state])
        steps = 0
        found = False
        
        while not found and queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                state = queue.popleft()
                
                for btn in buttons:
                    new_state = state ^ btn
                    
                    if new_state == 0:
                        steps += 1
                        found = True
                        break
                    
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append(new_state)
                
                if found:
                    break
            
            if found:
                break
            
            steps += 1
        
        total += steps
    
    return total

def gaussian_elimination(matrix):
    if not matrix:
        return [], []
    
    m = len(matrix)
    n = len(matrix[0]) - 1
    
    pivot_cols = []
    current_row = 0
    
    mat = [row[:] for row in matrix]
    
    for col in range(n):
        if current_row >= m:
            break
        
        pivot_row = -1
        for row in range(current_row, m):
            if mat[row][col] != 0:
                pivot_row = row
                break
        
        if pivot_row == -1:
            continue
        
        mat[current_row], mat[pivot_row] = mat[pivot_row], mat[current_row]
        pivot_cols.append(col)
        
        for row in range(current_row + 1, m):
            if mat[row][col] != 0:
                factor = mat[row][col]
                pivot_val = mat[current_row][col]
                
                for j in range(col, n + 1):
                    mat[row][j] = mat[row][j] * pivot_val - mat[current_row][j] * factor
        
        current_row += 1
    
    return pivot_cols, mat

def solve_system_exact(buttons, joltages):
    n = len(buttons)
    m = len(joltages)
    
    matrix = [[0] * (n + 1) for _ in range(m)]
    for i in range(m):
        for j in range(n):
            affects = False
            for pos in buttons[j]:
                if pos == i:
                    affects = True
                    break
            if affects:
                matrix[i][j] = 1
        matrix[i][n] = joltages[i]
    
    pivot_cols, reduced_matrix = gaussian_elimination(matrix)
    
    pivot_set = set(pivot_cols)
    free_vars = [i for i in range(n) if i not in pivot_set]
    
    best_solution = [0] * n
    best_sum = -1
    
    def try_solution(free_values):
        nonlocal best_solution, best_sum
        
        solution = [0] * n
        for i, var_idx in enumerate(free_vars):
            solution[var_idx] = free_values[i] if i < len(free_values) else 0
        
        for idx in range(len(pivot_cols) - 1, -1, -1):
            row = idx
            col = pivot_cols[idx]
            total = reduced_matrix[row][n]
            
            for j in range(col + 1, n):
                total -= reduced_matrix[row][j] * solution[j]
            
            if reduced_matrix[row][col] == 0:
                return
            
            if total % reduced_matrix[row][col] != 0:
                return
            
            val = total // reduced_matrix[row][col]
            if val < 0:
                return
            
            solution[col] = val
        
        for i in range(m):
            total = 0
            for j in range(n):
                if solution[j] > 0:
                    for pos in buttons[j]:
                        if pos == i:
                            total += solution[j]
                            break
            if total != joltages[i]:
                return
        
        total_presses = sum(solution)
        
        if best_sum == -1 or total_presses < best_sum:
            best_solution = solution[:]
            best_sum = total_presses
    
    if len(free_vars) == 0:
        try_solution([])
    elif len(free_vars) == 1:
        max_val = 0
        for j in joltages:
            if j > max_val:
                max_val = j
        max_val *= 3
        for val in range(max_val + 1):
            if best_sum != -1 and val > best_sum:
                break
            try_solution([val])
    elif len(free_vars) == 2:
        max_val = 0
        for j in joltages:
            if j > max_val:
                max_val = j
        if max_val < 200:
            max_val = 200
        for v1 in range(max_val + 1):
            for v2 in range(max_val + 1):
                if best_sum != -1 and v1 + v2 > best_sum:
                    continue
                try_solution([v1, v2])
    elif len(free_vars) == 3:
        for v1 in range(250):
            for v2 in range(250):
                for v3 in range(250):
                    if best_sum != -1 and v1 + v2 + v3 > best_sum:
                        continue
                    try_solution([v1, v2, v3])
    elif len(free_vars) == 4:
        for v1 in range(30):
            for v2 in range(30):
                for v3 in range(30):
                    for v4 in range(30):
                        if best_sum != -1 and v1 + v2 + v3 + v4 > best_sum:
                            continue
                        try_solution([v1, v2, v3, v4])
    else:
        try_solution([0] * len(free_vars))
    
    return 0 if best_sum == -1 else best_sum

def process_puzzle(machine):
    return solve_system_exact(machine["buttons"], machine["joltage"])

def solve_machines_part2(machines):
    if not machines:
        return 0
    
    num_workers = min(cpu_count(), len(machines))
    
    with Pool(processes=num_workers) as pool:
        results = pool.map(process_puzzle, machines)
    
    return sum(results)

if __name__ == '__main__':
    runner = SolutionRunner(FileReader)
    runner.run(solve_machines_part1, solve_machines_part2)
