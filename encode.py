#My name is Duong Nguyen and my lab partner is Jack Stone.


def encode_password(password):
    if len(password) != 8 or not password.isdigit():
        return "Invalid password format."

    encoded_password = ""
    for digit in password:
        new_digit = str((int(digit) + 3) % 10)
        encoded_password += new_digit

    return encoded_password


def decode_password(password):
    if len(password) != 8 or not password.isnumeric():
        return 'Invalid password format.'

    decoded_pass = ''
    for digit in password:
        decoded_pass += str((int(digit) - 3) % 10)

    return decoded_pass



