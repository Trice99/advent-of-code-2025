class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    ORANGE = '\033[38;5;208m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class OutputFormatter:
    @staticmethod
    def print_header(day_number=None):
        if day_number:
            print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*50}{Colors.END}")
            print(f"{Colors.BOLD}{Colors.YELLOW}Advent of Code - Day {day_number}{Colors.END}")
            print(f"{Colors.BOLD}{Colors.CYAN}{'='*50}{Colors.END}")
    
    @staticmethod
    def print_part(part_number, example_result, actual_result, example_time=None, input_time=None):
        print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*50}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.YELLOW}Part {part_number}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.CYAN}{'='*50}{Colors.END}")
        
        example_str = f"{Colors.BLUE}Example: {Colors.BOLD}{example_result}{Colors.END}"
        if example_time is not None:
            example_str += f" {Colors.ORANGE}({example_time:.4f}s){Colors.END}"
        print(example_str)
        
        answer_str = f"{Colors.GREEN}Answer:  {Colors.BOLD}{actual_result}{Colors.END}"
        if input_time is not None:
            answer_str += f" {Colors.ORANGE}({input_time:.4f}s){Colors.END}"
        print(answer_str)
    
    @staticmethod
    def print_results(example_part1, input_part1, example_part2, input_part2, 
                     example_time1=None, input_time1=None, example_time2=None, input_time2=None):
        OutputFormatter.print_part(1, example_part1, input_part1, example_time1, input_time1)
        OutputFormatter.print_part(2, example_part2, input_part2, example_time2, input_time2)


def print_part(part_number, example_result, actual_result, example_time=None, input_time=None):
    OutputFormatter.print_part(part_number, example_result, actual_result, example_time, input_time)
