from cp_otp import strxor
from cp_dictionary import list_of_words
from itertools import combinations


# Intercepted unintelligible ciphertexts
c1 = b'\x0b\x0e\x1e\x0b\x17'
c2 = b'\x15\x0a\x1b\x1d\x01'

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
# Hint: How is the ciphertext obtained, from the message?
#

## TODO Find possible word pairs.

## TODO Calculate encryption key.
