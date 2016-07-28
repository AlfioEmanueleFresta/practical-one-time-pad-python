from utils import strxor, strbin, ordinals_to_string, list_of_words
from itertools import combinations

# Ciphertexts
c1 = ordinals_to_string([11, 14, 30, 11, 23])
c2 = ordinals_to_string([21, 10, 27, 29, 1])

# Get a dictionary of words
words = list_of_words(of_length=len(c1))

# Get all combinations of two words in the dictionary
pairs = combinations(words, r=2)

# For all combinations
cx = strxor(c1, c2)
for m1, m2 in pairs:

    if strxor(m1, m2) == cx:
        print(m1, m2)

