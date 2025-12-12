
from common import SingleLineReader


class FileReader(SingleLineReader):
    def parse(self):
        lines = self.read_file()
        return self.get_ranges(lines)
    
    def get_ranges(self, lines):
        if not lines:
            return []
        raw = lines[0]
        parts = [p for p in raw.split(',') if p]
        ranges = []
        for p in parts:
            start, end = p.split('-')
            ranges.append((int(start), int(end)))
        return ranges
