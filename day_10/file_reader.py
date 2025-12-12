
from common import SingleLineReader


class FileReader(SingleLineReader):
    def parse(self):
        machines = []
        for line in self.read_file():
            machines.append(self.parse_machine_line(line))
        return machines

    def parse_machine_line(self, line):
        indicator_start = line.index("[")
        indicator_end = line.index("]")
        indicator_text = line[indicator_start + 1 : indicator_end]
        target = [1 if ch == "#" else 0 for ch in indicator_text]

        buttons = []
        i = indicator_end + 1

        while i < len(line):
            if line[i] == "(":
                j = line.index(")", i)
                raw = line[i + 1 : j].strip()
                if raw:
                    items = [int(x) for x in raw.split(",")]
                else:
                    items = []
                buttons.append(items)
                i = j + 1
            elif line[i] == "{":
                break
            else:
                i += 1

        joltage = []
        if "{" in line:
            joltage_start = line.index("{")
            joltage_end = line.index("}")
            joltage_text = line[joltage_start + 1 : joltage_end].strip()
            if joltage_text:
                joltage = [int(x) for x in joltage_text.split(",")]

        return {"target": target, "buttons": buttons, "joltage": joltage}
