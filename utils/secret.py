from time import sleep
from utils import strxor, get_random_string

_SECRET_KEY = False

SENDER_TAG =   "    SENDER:"
RECEIVER_TAG = "  RECEIVER:"

DETERRENT_SECONDS = 1


def _get_secret_key(length=None):

    global _SECRET_KEY

    if _SECRET_KEY:
        return _SECRET_KEY

    if not length:
        raise Exception("Can't generate a SECRET_KEY without a desired length.")

    _SECRET_KEY = get_random_string(length)
    return _SECRET_KEY


def intercept_in():

    input_message = "Online=1; UserIsPresident=0; ActivateSuperMassiveBlackHole=0;"

    print("%s A secret key has been generated and given, in person, to the other party." % SENDER_TAG)
    print("%s Sending:  '%s'" % (SENDER_TAG, input_message))

    sleep(DETERRENT_SECONDS)  # Deter brute forcing

    secret_key = _get_secret_key(len(input_message))
    ciphertext = strxor(input_message, secret_key)

    return ciphertext


def intercept_out(ciphertext):

    sleep(DETERRENT_SECONDS)

    secret_key = _get_secret_key()

    if len(ciphertext) != len(_SECRET_KEY):
        print("%s The received message length is invalid, something must have gone wrong." % RECEIVER_TAG)
        return

    message = strxor(ciphertext, secret_key)

    print("%s Received: '%s'" % (RECEIVER_TAG, message))

    is_online = "Online=1;" in message
    is_president = "UserIsPresident=1;" in message
    is_active = "ActivateSuperMassiveBlackHole=1;" in message

    if not is_online:
        print("%s ERROR - The device is offline." % RECEIVER_TAG)
        return

    if is_active and is_president:
        print("%s SUCCESS - Super Massive Black Hole activated." % RECEIVER_TAG)
        return

    elif is_active:
        print("%s ERROR - Authorisation denied. Only the President can do that." % RECEIVER_TAG)
        return

    elif is_president:
        print("%s IDLE - Hello Mr(s). President. I'll stand by for instructions." % RECEIVER_TAG)
        return

    else:
        print("%s IDLE." % RECEIVER_TAG)
        return
