def get_book_text(path):
    with open(path) as f:
        return (f.read())

def get_num_words(text):
        words = text.split()
        num_words = len(words)
        return num_words

def get_character_count(text):
    dicto = {}
        
    for char in text:
        char = char.lower()
        # check if already in dictionary
        if char in dicto:
            # increment count
            dicto[char] += 1
        elif char.isalpha():
            dicto.update({char: 1})
    return dicto

def sort_chars(char_dict):
    # Create a list of dictionaries
    chars_list = []
    for char, count in char_dict.items():
        if char.isalpha():  # Only include alphabetical characters
            chars_list.append({"char": char, "count": count})
    
    # Define the sort key function
    def sort_on(dict):
        return dict["count"]
    
    # Sort the list
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

def print_report(path):
    text = get_book_text(path)
    dicto = get_character_count(text)
    sorted_chars = sort_chars(dicto)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print(f"--------- Character Count -------")
    # Print each character and its count
    for char_info in sorted_chars:
        char = char_info["char"]
        count = char_info["count"]
        print(f"{char}: {count}")
    print(f"============= END ===============")