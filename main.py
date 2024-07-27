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


while __name__ == '__main__':
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()
    option = int(input('Please enter an option: '))
    if option == 1:
        password = input("Please enter the password to encode: ")
        encoded_password = encode(password)
        print('Your password has been encoded and stored!')
        print()
    elif option == 2:
        decoded_password = decode(encoded_password)
        print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        print()
    elif option == 3:
        exit()