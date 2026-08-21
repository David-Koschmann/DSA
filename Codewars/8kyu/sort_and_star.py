# You will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

# The returned value must be a string, and have "***" between each of its letters.

# You should not remove or add elements from/to the array.

def two_sort(array):
    # Sort the array and grab the first element
    first_word = sorted(array)[0]
    
    # Join each character of the word with "***"
    return "***".join(first_word)