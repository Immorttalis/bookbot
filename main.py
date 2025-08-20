from stats import get_word_count

def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
        return file_contents

def main():
    #print(get_book_text("books/frankenstein.txt"))
    print(f"{get_word_count(get_book_text("books/frankenstein.txt"))} words found in the document")
    

main()