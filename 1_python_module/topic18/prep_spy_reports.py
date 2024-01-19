from cryptography.fernet import Fernet


def create_key_and_save_to(file_name):
    key = Fernet.generate_key()
    with open(file_name, 'wb') as key_file:
        key_file.write(key)


if __name__ == '__main__':
    file_name = 'spy.key'
    create_key_and_save_to(file_name)
