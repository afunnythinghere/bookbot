from stats import number_of_words

from stats import num_characters

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = number_of_words(book_text)
    character_counts = num_characters(book_text)
    print(f"Found {num_words} total words")
    print(character_counts)
    






main()