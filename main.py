def main():
    # Get and print text 
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    # Get and print word count in text
    word_count = get_book_word_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document.\n\n")
    # Get and print character count in text
    char_count = get_character_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(char_count)

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

# Get text from provided path
def get_book_text(path):
    with open(path) as f:
        return f.read() 
    
# Find total word count in text
def get_book_word_count(text):
    words = text.split()
    return len(words)

# Find total character count per character in text
def get_character_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for c in num_chars_dict:
        sorted_list.append({"char": c, "num": num_chars_dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()