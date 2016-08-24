from cp_otp import strxor
import hashlib

try:
    from Crypto.Cipher import AES

except ImportError:  # OS X compatibility
    import crypto, sys
    sys.modules['Crypto'] = crypto
    from crypto.Cipher import AES


IV = b'\x97\xb8\xc7\xc6\x950\xb2j\x95\x80\x88\xa8\x8c\x1e\x0c\xa7'  # 16 random bytes


def keystream_generator(seed, key_length):
    """
    This generator implements a simple weak keystream generator
     based on the AES block cipher used repeatedly in ECB mode
     (somewhat similar to a CBC mode block cipher).

    :param seed: The seed for the generator. Needs to be a string or a bytes literal.
    :param key_length: The desired length in bytes for the keys in the keystream.
    :return: A key at each iteration of the generator.
    """

    # Make sure the seed is a bytes-literal.
    if type(seed) is str:
        seed = seed.encode('utf-8')

    # The seed must be made into a 32-bytes key.
    seed = hashlib.sha256(seed).hexdigest()[:32]

    # Create a simple ECB cipher
    ecb = AES.new(seed, AES.MODE_ECB)
    last_output = IV

    while True:
        output = b''
        while len(output) < key_length:  # Repeat until the key is long enough.
            output += ecb.encrypt(last_output)
            last_output = output
        yield output[:key_length]


