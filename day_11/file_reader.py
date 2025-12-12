
from common import SingleLineReader


class FileReader(SingleLineReader):
    def parse(self):
        lines = self.read_file()
        graph = {}
        for line in lines:
            parts = line.split(': ')
            device = parts[0]
            outputs = parts[1].split() if len(parts) > 1 else []
            graph[device] = outputs
        return graph
