from stats import *
from stats import get_book_text
import sys  

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        print_report(sys.argv[1])

main()