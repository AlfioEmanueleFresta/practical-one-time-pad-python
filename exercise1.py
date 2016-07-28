from utils import strxor, ordinals_to_string, list_of_words
from itertools import combinations


# Intercepted unintelligible ciphertexts
c1 = ordinals_to_string([11, 14, 30, 11, 23])
c2 = ordinals_to_string([21, 10, 27, 29, 1])

# Get a list of English words from a dictionary
words = list_of_words(of_length=len(c1))

# Get all combinations of two English words (pairs)
pairs = combinations(words, r=2)


#
# You have intercepted two messages encrypted using one-time pad (c1, c2).
#  Unfortunately, the parties have reused the same key for both messages.
#
# Find all possible pairs of English words that the parties may have communicated.
# You may find quite a few, but not all pairs will make sense.
#
# Note that you don't need to know the encryption key -- but once you
#  find a suitable candidate, you can calculate it!
#
# Hint: Remember that
#       A XOR B     equals    (A XOR C) XOR (B XOR C)
#
# Hint: How is the cipertext obtained, from the message?
#

## TODO Find possible word pairs.

## TODO Calculate encryption key.