def count_chars(text):
    characters = {}
    for c in text:
        if c not in characters:
            characters[c] = 1
        else:
            characters[c] += 1
    return characters


def retrieve_text(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text

def get_wordcount(text):
    words = text.split()
    return len(words)


    

def generate_report(filename):
    text = retrieve_text(filename)
    char_count = count_chars(text)
    word_count = get_wordcount(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n\n")
    for char, count in char_count.items():
        if char == '\n':
            char_display = '\\n'
        else:
            char_display = char
        print(f"the '{char_display}' character was found {count} times")
        
    print("--- End report ---")



def main():
    filename = 'books/frankenstein.txt'
    generate_report(filename)
    
        
        
if __name__ == '__main__':
    main()