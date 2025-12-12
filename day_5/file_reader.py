
from common import MultiLineReader


class FileReader(MultiLineReader):
    def parse(self):
        lines = self.read_file()
        return self.get_ranges_and_ids(lines)
    
    def get_ranges_and_ids(self, lines):
        ranges = []
        ids = []
        reading_ranges = True
        for line in lines:
            if line.strip() == '':
                reading_ranges = False
                continue
            if reading_ranges:
                start, end = line.split('-')
                ranges.append((int(start), int(end)))
            else:
                ids.append(int(line.strip()))
        return ranges, ids
