import sys
from stats import *

def get_book_text(path_to_file):
    with open(path_to_file) as f:
       return  f.read() 

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sort_list = get_sort_character(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sort_list:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

try: 
    main()
except IndexError:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    

    