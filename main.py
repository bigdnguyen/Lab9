from encode import decode_password, encode_password


def main():
    while True:
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')
        opt = int(input('Please enter an option: '))
        if opt == 3:
            exit()
        if opt == 1:
            password = (input('Please enter your password to encode: '))
            encoded_password = encode_password(password)
            print('Your password has been encoded and stored!\n')

        if opt == 2:
            decoded_password = decode_password(encoded_password)
            decode_password(password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.\n')


if __name__ == "__main__":
    main()
