import sys
from stats import count_words, count_characters,sort_dic



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1] #"/Users/andrewappiah/Documents/Projects/bookbot/books/frankenstein.txt"

    def get_book_text(path_to_book):
        with open(path_to_book) as file:
            return file.read()
        
    text_from_book = get_book_text(path_to_book)
    num_words = count_words(text_from_book)
    num_char = count_characters(text_from_book) 
    char_list = sort_dic(num_char)
    


    
    def print_stats(path_to_book, num_words, char_list):
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_book}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for dic in char_list:
            if dic["char"].isalpha() != True:
                    continue
        
            print(f"{dic["char"]}: {dic["num"]}")
        
        print("============= END ===============")
            
    print_stats(path_to_book, num_words, char_list)
    

























    
main()
    