
from common import MultiLineReader


class FileReader(MultiLineReader):
    def parse(self):
        lines = self.read_file()
        return self.get_points(lines)
    
    def get_points(self, lines):
        points = []
        for line in lines:
            if not line:
                continue
            parts = line.split(",")
            if len(parts) == 3:
                try:
                    x = int(parts[0])
                    y = int(parts[1])
                    z = int(parts[2])
                    points.append((x, y, z))
                except ValueError:
                    continue
        return points
