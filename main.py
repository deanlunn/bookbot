from stats import count_words, count_characters

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
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
        
    word_count = count_words(book_text)
    char_count = count_characters(book_text)
    
    print(f"{word_count} words found in the document")
    print(char_count)

if __name__ == "__main__":
    main()


