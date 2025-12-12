
from common import MultiLineReader


class FileReader(MultiLineReader):
    def parse(self):
        lines = self.read_file()
        shapes = {}
        idx = None
        buf = []
        regions = []
        mode = 0
        for line in lines:
            if not line:
                continue
            if ':' in line and 'x' not in line and line[0].isdigit():
                if idx is not None and buf:
                    shapes[idx] = buf
                idx = int(line[:-1])
                buf = []
                mode = 1
                continue
            if mode == 1:
                if line[0].isdigit() and 'x' in line:
                    if idx is not None and buf:
                        shapes[idx] = buf
                    buf = []
                    mode = 2
                else:
                    buf.append(line)
                    continue
            if mode == 2:
                size, rest = line.split(':')
                w, h = map(int, size.split('x'))
                qty = list(map(int, rest.split()))
                regions.append((w, h, qty))
        if idx is not None and buf:
            shapes[idx] = buf
        return shapes, regions
