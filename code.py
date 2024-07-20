import random
import string

def generate_password(length=16, complexity=4):
    """
    Generates a random password.

    Parameters:
    length (int): Length of the password. Default is 16.
    complexity (int): Complexity level of the password (1-4). Default is 4.
                      1 - Only lowercase letters
                      2 - Lowercase and uppercase letters
                      3 - Letters and digits
                      4 - Letters, digits, and punctuation

    Returns:
    str: Generated password
    """

    if complexity < 1 or complexity > 4:
        raise ValueError("Complexity must be between 1 and 4")

    char_sets = [
        string.ascii_lowercase,
        string.ascii_lowercase + string.ascii_uppercase,
        string.ascii_letters + string.digits,
        string.ascii_letters + string.digits + string.punctuation
    ]

    chars = char_sets[complexity - 1]

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Generated Password:", generate_password()) # type: ignore