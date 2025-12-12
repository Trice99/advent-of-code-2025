from .file_reader import FileReader
from common import SolutionRunner

def process_rotations(rotations):
    position = 50
    count_zero = 0

    for direction, distance in rotations:
        step = -1 if direction == 'L' else 1
        position = (position + step * distance) % 100
        if position == 0:
            count_zero += 1

    return count_zero

def count_zeros(rotations):
    position = 50
    count_zero = 0

    for direction, distance in rotations:
        step = -1 if direction == 'L' else 1
        for _ in range(distance):
            position = (position + step) % 100
            if position == 0:
                count_zero += 1

    return count_zero

if __name__ == '__main__':
    runner = SolutionRunner(FileReader)
    runner.run(process_rotations, count_zeros)
