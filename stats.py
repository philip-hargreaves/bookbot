def count_words(book_text):
    return len(book_text.split())

def count_letters(book_text):
    letter_freq = {}
    for word in book_text.split():
        for letter in word.lower():
            if letter.isalpha():
                letter_freq[letter] = letter_freq.get(letter, 0) + 1
    return letter_freq

def sort_dict(letter_freq):
    dict_list = []
    for key, value in letter_freq.items():
        formatted_dict = {"char": key, "num": value}
        dict_list.append(formatted_dict)
    
    def sort_on(letter_freq):
        return letter_freq["num"]

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
