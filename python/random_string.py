import random
import string

def generate_random_string(length):
    random_string = ''
    characters = string.ascii_letters + string.digits
    for _ in range(length):
        random_string = random_string + ''.join(random.choice(characters))
        #random_string = random_string + random.choice(characters)
    return random_string

# Example usage:
random_length = 10  # specify the length of the random string
random_str = generate_random_string(random_length)
print(f"Random string of length {random_length}: {random_str}")
