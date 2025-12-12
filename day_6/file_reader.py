
from common import MultiLineReader


class FileReader(MultiLineReader):
    def parse(self):
        lines = self.read_file()
        if not lines:
            return []
        return self._extract_blocks(lines, reversed_mode=False)
    
    def parse_reversed(self):
        lines = self.read_file()
        if not lines:
            return []
        return self._extract_blocks(lines, reversed_mode=True)

    def _extract_blocks(self, lines, reversed_mode):
        height = len(lines)
        width = max(len(line) for line in lines)
        padded = [line.ljust(width) for line in lines]

        problems = []
        col = 0
        while col < width:
            while col < width and all(padded[r][col] == " " for r in range(height)):
                col += 1
            if col >= width:
                break
            start = col
            while col < width and not all(padded[r][col] == " " for r in range(height)):
                col += 1
            end = col

            block = [padded[r][start:end] for r in range(height)]
            if reversed_mode:
                problems.append(self._parse_block_reversed(block))
            else:
                problems.append(self._parse_block(block))
        return problems

    def _parse_block(self, block):
        numbers = [int(row.rstrip()) for row in block[:-1] if row.strip()]
        op = block[-1].strip()
        return {"numbers": numbers, "op": op}

    def _parse_block_reversed(self, block):
        op = next((c for c in block[-1] if c in "+*"), None)
        if op is None:
            raise ValueError("No operator found in block")

        numbers = []
        height, width = len(block), len(block[0])
        for c in reversed(range(width)):
            digits = "".join(block[r][c] for r in range(height - 1) if block[r][c] != " ")
            if digits:
                numbers.append(int(digits))
        return {"numbers": numbers, "op": op}
