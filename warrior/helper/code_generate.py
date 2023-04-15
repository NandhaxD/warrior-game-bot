
import random
import string

def generate_random_string(10):
    code = random.choices(string.printable, k=length).encode('utf-8').decode()
    return code.replace(" ", "")

