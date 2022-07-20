import random
import string


def generateUser():    
    return ''.join(random.choice(string.digits) for i in range(5))