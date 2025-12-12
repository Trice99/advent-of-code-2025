
from common import MultiLineReader


class FileReader(MultiLineReader):
    def parse(self):
        return [list(line) for line in self.read_file() if line]
