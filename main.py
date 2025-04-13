def get_book_text(file_path):
    with open(file_path) as p:
        file_contents = p.read()
        return file_contents

def get_word_count(contents):
    split = contents.split()
    length = len(split)
    return length

def main():
    contents = get_book_text("books/frankenstein.txt")
    length = get_word_count(contents)
    
    print(f"{length} words found in the document")

main()
