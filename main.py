import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(filepath: str) -> str:
    """Reads the content of a file and returns it as a string."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"The file at {filepath} was not found.")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
        
    word_count = count_words(book_text)
    char_count = count_characters(book_text)
    sorted_chars = sort_characters(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
        
    for entry in sorted_chars:
        char = entry["char"]
        if char.isalpha():
            print(f"{char}: {entry['num']}")
            
    print("============= END ===============")

if __name__ == "__main__":
    main()


