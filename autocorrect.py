# Make sure you have NLTK installed. If not, run: !pip install nltk
import nltk
from nltk.metrics import edit_distance

nltk.download('words')

# Predefined vocabulary
vocabulary = set(nltk.corpus.words.words())

# Function to find the nearest word in the vocabulary
def find_nearest_word(word):
    min_distance = float('inf')
    nearest_word = None
    for vocab_word in vocabulary:
        distance = edit_distance(word, vocab_word)
        if distance < min_distance:
            min_distance = distance
            nearest_word = vocab_word
    return nearest_word

# Misspelled words
misspelled_words = ["acress", "neighbour", "seperated", "experiance"]

# Correct or suggest nearest words
corrected_words = {}
for word in misspelled_words:
    if word in vocabulary:
        corrected_words[word] = word
    else:
        nearest_word = find_nearest_word(word)
        corrected_words[word] = nearest_word

# Print results
for misspelled, corrected in corrected_words.items():
    print(f"Misspelled: {misspelled} | Corrected: {corrected}")
