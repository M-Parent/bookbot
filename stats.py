def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(items):
    return items["num"]

def get_sort_character(dict):
    sorted_list = []
    
    for char in dict:
        num = dict[char]
        item = {"char": char, "num": num}
        if char.isalpha():
            sorted_list.append(item)
        
        
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list       
        

    