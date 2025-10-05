def count_words(text_from_book):
    words = text_from_book.split()
    return len(words)

def count_characters(text_from_book):
    dict1 = {}
    for character in text_from_book.lower():
        if character not in dict1:
            dict1[character] = 1
        else:
            dict1[character] += 1
    return dict1

def sort_on(d):
    return d["num"]

def sort_dic(dict1):
    list1 = []
    for entry in dict1:
        list1.append({"char": entry, "num": dict1[entry]})
        list1.sort(reverse=True, key=sort_on)
    return list1    