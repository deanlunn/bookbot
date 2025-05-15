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

def sort_characters(char_count: dict) -> list:
    """
    Takes a dictionary of characters and their counts and returns a sorted list of dictionaries.
    Each dictionary contains 'char' and 'num' keys, sorted by count in descending order.
    """
    sorted_list = [{"char": char, "num": count} for char, count in char_count.items()]
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
