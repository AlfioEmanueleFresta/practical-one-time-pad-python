from time import sleep
from utils import strxor
from random import randint


SECRET_KEY = False

SENDER_TAG =   "    SENDER:"
RECEIVER_TAG = "  RECEIVER:"


def _get_secret_key(length=None):

    global SECRET_KEY

    if SECRET_KEY:
        return SECRET_KEY

    if not length:
        raise Exception("Can't generate a SECRET_KEY without a desired length.")

    SECRET_KEY = SECRET_KEY if SECRET_KEY else ''.join([chr(randint(0, 255)) for _ in range(0, length)])
    return SECRET_KEY


def intercept_in():
    input_message = "Online=1; UserIsPresident=0; ActivateSuperMassiveBlackHole=0;"
    print("%s Sending:  '%s'" % (SENDER_TAG, input_message))
    secret_key = _get_secret_key(len(input_message))
    return strxor(input_message, secret_key)


def intercept_out(ciphertext):

    sleep(2)  # Add a bit of suspence...

    if len(ciphertext) != len(SECRET_KEY):
        print("%s The received message length is invalid, something must have gone wrong." % RECEIVER_TAG)
        return

    secret_key = _get_secret_key()
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
        print("%s IDLE - Status report received, thanks." % RECEIVER_TAG)
        return
