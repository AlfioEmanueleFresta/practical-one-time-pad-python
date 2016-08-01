import hashlib
from random import randint

MAX_ORDINAL = 255
MAX_ORDINAL_ERROR = "Characters need to be in ordinal range 0-255 (8 bit)."


def strxor(s1, s2):
    """
    Bitwise XOR two strings. Strings can have at most 8 bit characters.
    :param s1: First string.
    :param s2: Second string.
    :return: First string bitwise XOR.
    """
    output = ""

    if len(s1) != len(s2):
        raise ValueError("Length mismatch. len('%s')=%d, len('%s')=%d." %
                         (s1, len(s1), s2, len(s2)))

    for a, b in zip(s1, s2):

        ord_a, ord_b = ord(a), ord(b)

        if ord_a > MAX_ORDINAL or ord_b > MAX_ORDINAL:
            raise ValueError(MAX_ORDINAL_ERROR)

        # ^ is bitwise XOR in Python
        output += chr(ord_a ^ ord_b)

    return output


def strbin(s, separator=' '):
    """
    Return a nice string of bytes for display.
    :param s: The string.
    :param separator: The separator, if any.
    :return: Binary representation of character bytes, separated by a space.
    """
    return separator.join("{:08b}".format(ord(x)) for x in s)


def strpad(s, length, padding=' '):
    """
    Pads a string up to a given length.
    :param s: The string to pad.
    :param length: The desired length.
    :param padding: The padding character to use.
    :return:
    """
    while len(s) < length:
        s += padding
    return s


def ordinals_to_string(list):
    """
    Returns a string from a list of ordinals.
    :param list: List of ordinals.
    :return: A string
    """
    output = ""

    for c in list:

        if c > MAX_ORDINAL:
            raise ValueError(MAX_ORDINAL_ERROR)

        output += chr(c)

    return output


def list_of_words(of_length=None):
    """
    Returns a list of words from a dictionary.
    :param of_length: Length. If not specified, all words will be returned.
    :return: A list of lowercase words.
    """

    if of_length:
        dictionary_file = "utils/dictionary/words%d.txt" % of_length
    else:
        dictionary_file = "utils/dictionary/words.txt"

    try:
        dictionary = open(dictionary_file, 'r')
        words = [x.rstrip('\n') for x in dictionary.readlines()]
        dictionary.close()

    except IOError:
        raise Exception("Unable to find or read dictionary (%s)." % dictionary_file)

    return words


def get_random_string(length, ord_min=0, ord_max=255):
    """
    A method to get a random string. Characters are distributed in the range specified
    by ord_min and ord_max, and python's randint is used to get the string -- therefore this
    method is not cryptographically secure.
    :param length: Length of the string.
    :param ord_min: Minimum ordinal.
    :param ord_max: Maximum ordinal, i.e., 128 for ASCII, 256 for UTF-8.
    :return:
    """
    return ''.join([chr(randint(ord_min, ord_max)) for _ in range(0, length)])


get_human_readable_random_string = lambda length: get_random_string(length, 48, 91)


def key_stream_generator(key_length, seed):
    """
    Returns a generator for a key stream, given the seed value
    and the desired key length.

    NOTE: This is NOT secure. In particular, the key only uses HEX characters.
          A part from using a CSPRNG, the returned key should cover the whole range of available
          characters and be randomly distributed.

    :param key_length: A positive integer for the key.
    :param seed: The initial seed for the key generator. Identical seed will result in identical keys.
    :return: A generator for a key stream.
    """
    def generate():
        last_key = seed
        while True:
            next_key = ""
            while len(next_key) < key_length:
                next_key += hashlib.sha1((next_key if next_key else last_key).encode('utf-8')).hexdigest()
            yield next_key[:key_length]
            last_key = next_key
    return generate()

