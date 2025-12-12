
from common import SingleLineReader


class FileReader(SingleLineReader):
    def parse(self):
        return self.read_file()
