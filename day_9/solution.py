from .file_reader import FileReader
from common import SolutionRunner

def point_in_polygon(x, y, polygon):
    inside = False
    px, py = polygon[-1]
    for cx, cy in polygon:
        if min(py, cy) < y <= max(py, cy) and x <= max(px, cx) and py != cy:
            if x <= (y - py) * (cx - px) / (cy - py) + px:
                inside = not inside
        px, py = cx, cy
    return inside

def build_boundary_set(polygon):
    boundary = set()
    px, py = polygon[-1]
    for cx, cy in polygon:
        if px == cx:
            boundary.update((px, y) for y in range(min(py, cy), max(py, cy) + 1))
        else:
            boundary.update((x, py) for x in range(min(px, cx), max(px, cx) + 1))
        px, py = cx, cy
    return boundary

def is_valid_rectangle(x1, y1, x2, y2, boundary, polygon, cache):
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)
    
    corners = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]
    for pt in corners:
        if pt not in boundary:
            if pt not in cache:
                cache[pt] = point_in_polygon(pt[0], pt[1], polygon)
            if not cache[pt]:
                return False
    
    w, h = max_x - min_x + 1, max_y - min_y + 1
    step_x, step_y = max(1, w // 100), max(1, h // 100)
    
    for x in range(min_x, max_x + 1, step_x):
        for y in (min_y, max_y):
            pt = (x, y)
            if pt not in boundary:
                if pt not in cache:
                    cache[pt] = point_in_polygon(x, y, polygon)
                if not cache[pt]:
                    return False

    for y in range(min_y, max_y + 1, step_y):
        for x in (min_x, max_x):
            pt = (x, y)
            if pt not in boundary:
                if pt not in cache:
                    cache[pt] = point_in_polygon(x, y, polygon)
                if not cache[pt]:
                    return False

    return True

def max_rectangle_area(points):
    if not points:
        return 0
    max_area = 0
    n = len(points)
    
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if area > max_area:
                max_area = area
    
    return max_area

def point_in_polygon(x, y, polygon):
    inside = False
    px, py = polygon[-1]
    for cx, cy in polygon:
        if min(py, cy) < y <= max(py, cy) and x <= max(px, cx) and py != cy:
            if x <= (y - py) * (cx - px) / (cy - py) + px:
                inside = not inside
        px, py = cx, cy
    return inside

def build_boundary_set(polygon):
    boundary = set()
    px, py = polygon[-1]
    for cx, cy in polygon:
        if px == cx:
            boundary.update((px, y) for y in range(min(py, cy), max(py, cy) + 1))
        else:
            boundary.update((x, py) for x in range(min(px, cx), max(px, cx) + 1))
        px, py = cx, cy
    return boundary

def is_valid_rectangle(x1, y1, x2, y2, boundary, polygon, cache):
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)
    
    corners = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]
    for pt in corners:
        if pt not in boundary:
            if pt not in cache:
                cache[pt] = point_in_polygon(pt[0], pt[1], polygon)
            if not cache[pt]:
                return False
    
    w, h = max_x - min_x + 1, max_y - min_y + 1
    step_x, step_y = max(1, w // 100), max(1, h // 100)
    
    for x in range(min_x, max_x + 1, step_x):
        for y in (min_y, max_y):
            pt = (x, y)
            if pt not in boundary:
                if pt not in cache:
                    cache[pt] = point_in_polygon(x, y, polygon)
                if not cache[pt]:
                    return False

    for y in range(min_y, max_y + 1, step_y):
        for x in (min_x, max_x):
            pt = (x, y)
            if pt not in boundary:
                if pt not in cache:
                    cache[pt] = point_in_polygon(x, y, polygon)
                if not cache[pt]:
                    return False

    return True

def max_constrained_rectangle_area(points):
    if not points:
        return 0
    
    boundary = build_boundary_set(points)
    n = len(points)
    max_area = 0
    cache = {}
    
    sorted_points = sorted(points, key=lambda p: (p[0], p[1]))
    
    for i in range(n - 1):
        x1, y1 = sorted_points[i]
        best_for_i = 0
        
        for j in range(n - 1, i, -1):
            x2, y2 = sorted_points[j]
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            
            if area <= max_area or area <= best_for_i:
                continue
                
            if is_valid_rectangle(x1, y1, x2, y2, boundary, points, cache):
                max_area = area
                best_for_i = area
    
    return max_area

if __name__ == '__main__':
    runner = SolutionRunner(FileReader)
    runner.run(max_rectangle_area, max_constrained_rectangle_area)
