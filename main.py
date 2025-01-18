def main():
    book_path = r"books/frankenstein.txt"
    text = get_text(book_path)
    num_words = get_num_words(text)
    letter_dict = get_letter_count(text)
    #Letters only and sort using list
    alpha_list = []
    for k in letter_dict:
        if k.isalpha() == True:
            single_entry = {"letter":k, "count": letter_dict[k]}
            alpha_list.append(single_entry)
    alpha_list.sort(reverse=True, key=sort_on)

    #Report Generation
    print(f"--- Begin report of {book_path}")
    print(f"{num_words} words found in the document")
    print("")
    for dict in alpha_list:
        print(f"The '{dict["letter"]}' character was found {dict["count"]} times")
    print("--- End report---")

def get_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return (len(words))

def get_letter_count(text):
    lowered_text = text.lower()
    letters = {}
    for i in lowered_text:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters

def sort_on(dict):
    return dict["count"]

main()