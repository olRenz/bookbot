import sys
from stats import word_count, sort_list


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    num_words = word_count(file_path)
    letter_dict = sort_list(file_path)
    
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for pairs in letter_dict:
            print(pairs)
    print('============= END ===============')

main()