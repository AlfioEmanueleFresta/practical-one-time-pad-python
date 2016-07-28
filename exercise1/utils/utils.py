
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

