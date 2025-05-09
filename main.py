from stats import get_word_count
from stats import get_book_text
from stats import character_count
from stats import print_report
from sys import argv
import sys



def main():
 
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print_report(argv[1])

main()
