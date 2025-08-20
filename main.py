def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
        return file_contents

def get_word_count(texts):
    to_count = texts.split()
    word_count = 0
    for text in to_count:
        word_count += 1
    return word_count

def main():
    #print(get_book_text("books/frankenstein.txt"))
    print(f"{get_word_count(get_book_text("books/frankenstein.txt"))} words found in the document")
    

main()