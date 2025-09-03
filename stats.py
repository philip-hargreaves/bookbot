def count_words(book_text):
    return len(book_text.split())

def count_letters(book_text):
    letter_freq = {}
    for word in book_text.split():
        for letter in word.lower():
            letter_freq[letter] = letter_freq.get(letter, 0) + 1
    return letter_freq