
import random
import string

def generate_random_string():
    return "".join(random.choices(string.printable, k=10)).encode('utf-8').decode()

