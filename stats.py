def count_words(text: str) -> int:
    """Returns the number of words in the given text."""
    num_words = text.split()
    return len(num_words)

def count_characters(text: str) -> dict:
    """Returns a dictionary with the count of each character in the text, case insensitive."""
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count