def get_word_count(contents):
    split = contents.split()
    length = len(split)
    return length

def num_characters(contents):
    counted_chars = dict.fromkeys(contents.lower(), 0)
    
    for char in contents:
        counted_chars[char.lower()] += 1

    return counted_chars

def dict_sort(input_dict):
    dict_list = []
    for item in input_dict:
        dict_list.append({'char':item, 'num':input_dict[item]})
    dict_list.sort(reverse=True, key=sort_on)

    return dict_list

def sort_on(dict):
    return dict["num"]
