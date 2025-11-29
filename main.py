from stats import number_of_words

from stats import num_characters

from stats import sort_on

from stats import sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = number_of_words(book_text)
    character_counts = num_characters(book_text)
    report = sorted_list(character_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for repor in report:
        current_char = repor["char"]
        if not current_char.isalpha():
            continue
        current_num = repor["num"] 
        print(f"{current_char}: {current_num}")
    print("============= END ===============")

    





main()