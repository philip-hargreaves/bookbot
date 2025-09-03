from stats import count_words, count_letters

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents


def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = count_words(book_text)
    print(f"{word_count} words found in the document")

    letter_freq = count_letters(book_text)
    print(letter_freq)



main()