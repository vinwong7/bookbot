from stats import get_num_words, get_chars_dict, sort_dict
import sys

def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
    return book_text

def print_report(book_path, num_words, chars_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for x in chars_list:
       print(x["letter"] + ": " + str(x["num"]) )

def main():
   if len(sys.argv) < 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
   book_path = sys.argv[1]
   text = get_book_text(book_path)
   num_words = get_num_words(text)
   chars_dict = get_chars_dict(text)
   chars_list = sort_dict(chars_dict) 
   print_report(book_path, num_words, chars_list)

   

main()