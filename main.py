def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
        return file_contents
def main():
    print(get_book_text("books/frankenstein.txt"))
    

main()