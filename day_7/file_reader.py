
from common import MultiLineReader


class FileReader(MultiLineReader):
    def parse(self):
        lines = self.read_file()
        return [line for line in lines if line]
