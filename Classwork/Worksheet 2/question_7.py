import random
import string

def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

for _ in range(100):
    length = random.randint(6, 8)
    print(random_string(length))