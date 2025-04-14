from stats import get_word_count, num_characters, dict_sort

def get_book_text(file_path):
    with open(file_path) as p:
        file_contents = p.read()
        return file_contents

def main():
    contents = get_book_text("books/frankenstein.txt")
    length = get_word_count(contents)
    chars = num_characters(contents)
    print("========= BOOKBOT =========")
    print("Analyzing book found in books folder")
    print("--------- Word Count ---------")
    print(f"Found {length} total words")
    print("--------- Character Count ---------")
    report = dict_sort(chars)
    for item in report:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

main()
