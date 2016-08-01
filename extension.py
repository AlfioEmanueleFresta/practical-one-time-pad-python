from utils import key_stream_generator, get_random_string, get_human_readable_random_string, strpad
from utils import strxor

MESSAGES_LENGTH = 128

stream = key_stream_generator(MESSAGES_LENGTH, "Secret seed")


for key, _ in zip(stream, range(0, 10)):

    message = strpad(get_human_readable_random_string(60), MESSAGES_LENGTH)
    ciphertext = strxor(message, key)

    print("    Message: %s" % message)
    #print(" Ciphertext: %s" % ciphertext)

    recovered = strxor(ciphertext, key)
    print("  Recovered: %s" % recovered)

    assert message == recovered