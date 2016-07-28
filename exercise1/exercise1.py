from utils import strxor, strbin, ordinals_to_string, list_of_words
from itertools import combinations

# Ciphertexts
c1 = ordinals_to_string([11, 14, 30, 11, 23])
c2 = ordinals_to_string([21, 10, 27, 29, 1])

# Get a dictionary of words
words = list_of_words(of_length=len(c1))

# Get all combinations of two words in the dictionary
pairs = combinations(words, r=2)

# Write your code here.

## TODO Find possible word pairs.

## TODO Calculate encryption key.

#
# You need to find candidate pairs of words.
# You'll find a few of these, but not all will make sense.
#
# You don't need to know the encryption key -- but once you
#  find a suitable candidate, you can calculate it.
#
# Hint: Remember that
#       A XOR B     equals    (A XOR C) XOR (B XOR C)
#
# Hint: How is the cipertext obtained, from the message?
#