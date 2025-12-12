import os
import sys
import subprocess
from common import Colors


def run_day(day_number):
    day_dir = f"day_{day_number}"
    day_path = os.path.join(os.path.dirname(__file__), day_dir)
    
    if not os.path.exists(day_path):
        return None
    
    solution_file = os.path.join(day_path, "solution.py")
    if not os.path.exists(solution_file):
        return None
    
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.YELLOW}Running Day {day_number}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.END}")
    
    try:
        result = subprocess.run(
            [sys.executable, '-m', f'day_{day_number}.solution'],
            cwd=os.path.dirname(__file__),
            capture_output=True,
            text=True,
            timeout=300,
            env={**os.environ, 'PYTHONPATH': os.path.dirname(__file__)}
        )
        
        if result.returncode == 0:
            print(result.stdout)
            return {'day': day_number, 'status': 'success'}
        else:
            print(f"{Colors.RED}Error running day {day_number}:{Colors.END}")
            print(result.stderr)
            return {'day': day_number, 'status': 'error'}
    except subprocess.TimeoutExpired:
        print(f"{Colors.RED}Timeout: Day {day_number} exceeded 5 minutes{Colors.END}")
        return {'day': day_number, 'status': 'timeout'}
    except Exception as e:
        print(f"{Colors.RED}Exception running day {day_number}: {e}{Colors.END}")
        return {'day': day_number, 'status': 'exception'}


def print_summary(results):
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.YELLOW}Summary{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.END}\n")
    
    success_count = 0
    
    for result in results:
        if result:
            day = result['day']
            status = result['status']
            
            if status == 'success':
                success_count += 1
                status_str = f"{Colors.GREEN}✓{Colors.END}"
            elif status == 'error':
                status_str = f"{Colors.RED}✗{Colors.END}"
            elif status == 'timeout':
                status_str = f"{Colors.YELLOW}⏱{Colors.END}"
            else:
                status_str = f"{Colors.RED}!{Colors.END}"
            
            print(f"{status_str} Day {day:2d}")
    
    print(f"\n{Colors.BOLD}Total Days: {len(results)}{Colors.END}")
    print(f"{Colors.BOLD}Successful: {Colors.GREEN}{success_count}{Colors.END}")


def main():
    print(f"{Colors.BOLD}{Colors.HEADER}")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║           Advent of Code 2025 - All Solutions           ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print(f"{Colors.END}")
    
    results = []
    for day in range(1, 13):
        result = run_day(day)
        if result:
            results.append(result)
    
    print_summary(results)
    
    print(f"\n{Colors.BOLD}{Colors.GREEN}All days completed!{Colors.END}\n")


if __name__ == '__main__':
    main()
