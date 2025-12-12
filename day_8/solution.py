from .file_reader import FileReader
import math
from common import OutputFormatter
import time

def distance(point_a, point_b):
    return math.sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2 + (point_a[2] - point_b[2])**2)

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, node_a, node_b):
        root_a = self.find(node_a)
        root_b = self.find(node_b)
        if root_a == root_b:
            return False
        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        elif self.rank[root_b] < self.rank[root_a]:
            self.parent[root_b] = root_a
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1
        return True

def compute_circuits(points, pair_count):
    num_points = len(points)
    if num_points == 0:
        return 0

    union_find = UnionFind(num_points)

    edges = []
    for i in range(num_points):
        for j in range(i + 1, num_points):
            dist = distance(points[i], points[j])
            edges.append((dist, i, j))

    edges.sort(key=lambda edge: edge[0])

    for index in range(min(pair_count, len(edges))):
        dist, node_a, node_b = edges[index]
        union_find.union(node_a, node_b)

    circuit_sizes = {}
    for i in range(num_points):
        root = union_find.find(i)
        circuit_sizes[root] = circuit_sizes.get(root, 0) + 1

    sizes = sorted(circuit_sizes.values(), reverse=True)
    if len(sizes) < 3:
        return 0

    return sizes[0] * sizes[1] * sizes[2]

def find_last_connection(points):
    num_points = len(points)
    if num_points == 0:
        return 0

    union_find = UnionFind(num_points)

    edges = []
    for i in range(num_points):
        for j in range(i + 1, num_points):
            dist = distance(points[i], points[j])
            edges.append((dist, i, j))

    edges.sort(key=lambda edge: edge[0])

    num_circuits = num_points
    for dist, node_a, node_b in edges:
        if union_find.union(node_a, node_b):
            num_circuits -= 1
            if num_circuits == 1:
                return points[node_a][0] * points[node_b][0]

    return 0

if __name__ == '__main__':
    example_reader = FileReader('example.txt')
    input_reader = FileReader('input.txt')

    example_data = example_reader.parse()
    input_data = input_reader.parse()

    start = time.time()
    example_part1 = compute_circuits(example_data, 10)
    example_time1 = time.time() - start
    start = time.time()
    input_part1 = compute_circuits(input_data, 1000)
    input_time1 = time.time() - start
    OutputFormatter.print_part(1, example_part1, input_part1, example_time1, input_time1)

    start = time.time()
    example_part2 = find_last_connection(example_data)
    example_time2 = time.time() - start
    start = time.time()
    input_part2 = find_last_connection(input_data)
    input_time2 = time.time() - start
    OutputFormatter.print_part(2, example_part2, input_part2, example_time2, input_time2)
