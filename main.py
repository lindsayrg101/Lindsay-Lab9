def encode(password):
    encoded_password = ""
    for char in password:
        new_char = str((int(char) + 3) % 10)
        encoded_password += new_char
    return encoded_password


def decode(password):
    decoded = ""
    for char in password:
        new_char = str(int(char) - 3)
        decoded += new_char
    return decoded


