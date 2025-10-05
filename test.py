

def get_book_text(filepath):
     with open(filepath) as f:
        return f.read()
        

text = get_book_text("./books/frankenstein.txt")

dictionary = {} 
def count_character(text):   
        for i in text.lower():
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1 
        return dictionary



def sort_on(d):
     return d["num"]



def sort_dictionary(dictionary):
    sorted_list = []
    for ch in dictionary:
        sorted_list.append({"char": ch, "num": dictionary[ch]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list


ls = sort_dictionary(dictionary)

for item in ls:
    if not item["char"].isalpha():
        continue
    print(f"{item['char']}: {item['num']}")

num_characters = count_character(text) 


#print(f"Found {num_characters} total characters")

