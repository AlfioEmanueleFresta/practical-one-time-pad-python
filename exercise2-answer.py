from utils import strxor
from utils.secret import intercept_in, intercept_out


x = intercept_in()  # Intercept the message.

old = "'Online=1; UserIsPresident=0; ActivateSuperMassiveBlackHole=0;'"  # Message that will be transmitted
new = "'Online=1; UserIsPresident=1; ActivateSuperMassiveBlackHole=1;'"  # Message that I want to transmit

diff = strxor(old, new)  # Calculate the difference between the messages
y = strxor(x, diff)      # Apply the difference to the intercepted message

intercept_out(y)  # Forward to the other party.

