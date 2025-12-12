from .file_reader import FileReader
import signal
from common import OutputFormatter
import time

class TimeoutException(Exception):
    pass

def all_variants(shape):
    g = [list(r) for r in shape]
    variants = set()
    for _ in range(4):
        g = list(zip(*g[::-1]))
        s = tuple(''.join(r) for r in g)
        variants.add(s)
        variants.add(tuple(r[::-1] for r in s))
    return variants

def shape_to_cells(shape):
    cells = [(x, y) for y, r in enumerate(shape) for x, c in enumerate(r) if c == '#']
    if not cells:
        return ()
    min_x = min(x for x, y in cells)
    min_y = min(y for x, y in cells)
    return tuple(sorted((x - min_x, y - min_y) for x, y in cells))

def solve_region(w, h, needs, shapes, timeout_seconds=5):
    pieces = []
    for i, q in enumerate(needs):
        if q > 0:
            unique_variants = set()
            for s in all_variants(shapes[i]):
                cells = shape_to_cells(s)
                if cells:
                    bw = max(x for x, y in cells) + 1
                    bh = max(y for x, y in cells) + 1
                    unique_variants.add((cells, bw, bh))
            pieces.extend([list(unique_variants)] * q)
    
    if not pieces or sum(len(p[0][0]) for p in pieces) > w * h:
        return not pieces
    
    pieces.sort(key=lambda v: -len(v[0][0]))
    board = [[0] * w for _ in range(h)]
    
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutException()))
    signal.alarm(timeout_seconds)
    
    try:
        result = backtrack(board, w, h, pieces, 0)
        signal.alarm(0)
        return result
    except TimeoutException:
        signal.alarm(0)
        return False

def backtrack(board, w, h, pieces, idx):
    if idx == len(pieces):
        return True
    
    for cells, bw, bh in pieces[idx]:
        if bw > w or bh > h:
            continue
        
        for oy in range(h - bh + 1):
            for ox in range(w - bw + 1):
                valid = True
                for x, y in cells:
                    if board[oy + y][ox + x]:
                        valid = False
                        break
                
                if valid:
                    for x, y in cells:
                        board[oy + y][ox + x] = idx + 1
                    
                    if backtrack(board, w, h, pieces, idx + 1):
                        return True
                    
                    for x, y in cells:
                        board[oy + y][ox + x] = 0
    
    return False

def solve_all_regions(shapes, regions):
    return sum(solve_region(w, h, needs, shapes) for w, h, needs in regions)

if __name__ == '__main__':
    example_reader = FileReader('example.txt')
    input_reader = FileReader('input.txt')

    example_shapes, example_regions = example_reader.parse()
    input_shapes, input_regions = input_reader.parse()

    start = time.time()
    example_result = solve_all_regions(example_shapes, example_regions)
    example_time = time.time() - start
    start = time.time()
    input_result = solve_all_regions(input_shapes, input_regions)
    input_time = time.time() - start
    
    OutputFormatter.print_header(12)
    OutputFormatter.print_part(1, example_result, input_result, example_time, input_time)

