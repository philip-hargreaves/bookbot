from stats import count_words, count_letters, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text = get_book_text(sys.argv[1])
    word_count = count_words(book_text)

    letter_freq = count_letters(book_text)
    formatted_letter_freq = sort_dict(letter_freq)

    # Print header
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...")
    # Print word count
    print(f"----------- Word Count ----------\nFound {word_count} total words")
    # Print character count
    print("--------- Character Count -------")
    for letter in formatted_letter_freq:
            print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")


main()