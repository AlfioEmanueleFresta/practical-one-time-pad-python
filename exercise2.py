from utils import strxor
from utils.secret import intercept_in, intercept_out


ciphertext = intercept_in()

# TODO Change ciphertext to activate...

intercept_out(ciphertext)

