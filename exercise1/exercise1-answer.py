from utils import strxor, ordinals_to_string, list_of_words
from itertools import combinations

# Ciphertexts
c1 = ordinals_to_string([11, 14, 30, 11, 23])
c2 = ordinals_to_string([21, 10, 27, 29, 1])

# Get a dictionary of words
words = list_of_words(of_length=len(c1))

# Get all combinations of two words in the dictionary
pairs = combinations(words, r=2)

# Get C1 XOR C2
c1_xor_c2 = strxor(c1, c2)

for m1, m2 in pairs:

    # Calculate the difference between the words
    m1_xor_m2 = strxor(m1, m2)

    # If (M1 XOR M2) == (C1 XOR C2), this is a candidate.
    # This is because (C1 XOR C2) == (M1 XOR K1) XOR (M2 XOR K2)
    if m1_xor_m2 == c1_xor_c2:

        # Calculate the key
        key = strxor(m1, c1)

        # Announce our exiting discovery.
        print("Candidate found: m1='%s', m2='%s', key='%s'"
              % (m1, m2, key))

