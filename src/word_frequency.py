

def read_input_file(file_path):
    """Reads the input text from a specified file."""
    with open(file_path, 'r') as file:
        return file.read()

def compute_word_frequency(text):
    """Computes the frequency of words in the given text."""
    # Remove punctuation and split the text into words
    words = text.split()
    frequency = {}

    for word in words:
        word = word.lower()  # Convert to lower case
        frequency[word] = frequency.get(word, 0) + 1

   
    sorted_frequency = dict(sorted(frequency.items()))
    return sorted_frequency
