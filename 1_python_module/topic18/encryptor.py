import os

from cryptography.fernet import Fernet


def load_key():
    return open('spy.key', 'rb').read()


def encrypt(filename, key):
    f = Fernet(key)

    with open(filename, 'rb') as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename, 'wb') as file:
        file.write(encrypted_data)


if __name__ == '__main__':
    key = load_key()

    base_path = "spy_reports"
    filenames = os.listdir(base_path)
    print(filenames)
    for filename in filenames:
        encrypt(base_path + "/" + filename, key)
