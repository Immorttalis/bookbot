from stats import get_word_count
from stats import get_letter_count
from stats import get_dict_list
from stats import list_sort
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
        return file_contents




def main():
    
    #input prompt
    if len(sys.argv) == 2:
        print("Correct number of arguments.")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    args = sys.argv

    #print(get_book_text("books/frankenstein.txt"))
    print("============ BOOKBOT ============\n"
          f"Analyzing book found at {args[1]}...\n"
          "----------- Word Count ----------")
    word_count = get_word_count(get_book_text(f"{args[1]}"))
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    letter_count = get_letter_count(get_book_text(f"{args[1]}"))
    dict_list = get_dict_list(get_letter_count(get_book_text(f"{args[1]}")))
    dict_list.sort(reverse=True, key=list_sort)
    
    #truncating the list of dictionaries to display just the relevant data
    trunc_list = [user["char"] for user in dict_list]
    trunc_list2 = [user["num"] for user in dict_list]
    
    #making print visually appealing (ripped off of https://stackoverflow.com/questions/58400388/how-do-i-print-list-items-from-two-separate-lists-on-the-same-line)
    for i in range(len(trunc_list)):
        print(f"{trunc_list[i]}: {trunc_list2[i]}")


main()