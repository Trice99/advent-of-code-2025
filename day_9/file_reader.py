
from common import SingleLineReader


class FileReader(SingleLineReader):
    def parse(self):
        lines = self.read_file()
        return self.get_points(lines)
    
    def get_points(self, lines):
        points = []
        for line in lines:
            if "," in line:
                x, y = line.split(",")
                try:
                    points.append((int(x), int(y)))
                except ValueError:
                    pass
        return points
