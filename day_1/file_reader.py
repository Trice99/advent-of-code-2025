
from common import SingleLineReader


class FileReader(SingleLineReader):
    def parse(self):
        lines = self.read_file()
        return self.get_rotations(lines)
    
    def get_rotations(self, lines):
        rotations = []
        for line in lines:
            direction = line[0]
            distance = int(line[1:])
            rotations.append((direction, distance))
        return rotations
