from itertools import permutations
import string


def algo():
    pwType = input("Is your password just letters and numbers?").upper()
    if pwType == 'YES':
        alphaChar = list(string.ascii_letters)+["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    else:
        alphaChar = list(string.printable)

    charCount = int(input("how many characters is your password"))
    pw = list(permutations(alphaChar, charCount))
    d = [''.join(x) for x in pw]
    return d
