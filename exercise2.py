from utils import strxor
from utils.secret import intercept_in, intercept_out


x = intercept_in()  # Intercept the message.

#
# You have found a way to intercept a one-time pad encrypted message between two
#  parties: a control station (SENDER) and a powerful top-secret CERN computer (RECEIVER).
#
# You don't know the key, but you know what the message contains. You should NOT try to find the key.
# You want to change the message so that the RECEIVER activates a super massive black hole.
#
# Hint: Execute this script and listen to what the parties say to each other.
#
# Hint: What's the 'difference' between what's being transmitted and what you want to
#       be received?
#

y = x  # TODO

intercept_out(y)  # Forward to the other party.
