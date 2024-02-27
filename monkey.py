import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=length))

def monkey_typing(target):
    target_length = len(target)
    attempt = ''
    attempts = 0

    while attempt != target:
        attempt = generate_random_string(target_length)
        print(attempt)
        attempts += 1

    print(f"\nMonkey successfully typed '{target}' in {attempts} attempts!")


