def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        if c.lower() in chars:
            chars[c.lower()] += 1
        else:
            chars[c.lower()] = 1
    return chars    

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    final_list = []
    for k, v in dict.items():
        if k.isalpha() == False:
            pass
        else:
            char_dict = {}
            char_dict["letter"] = k
            char_dict["num"] = v
            final_list.append(char_dict)
    final_list.sort(reverse=True, key=sort_on)
    return final_list