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
    
def count_words(text: str) -> int:
    """Returns the number of words in the given text."""
    num_words = text.split()
    return len(num_words)
    
def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    print(f"{count_words(book_text)} words found in the document")

if __name__ == "__main__":
    main()

