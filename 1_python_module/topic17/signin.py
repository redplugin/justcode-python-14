import os

from dotenv import load_dotenv

from instagram import Instagram


# load_dotenv(dotenv_path=".env.example")
load_dotenv(dotenv_path="/1_python_module/topic17/.env")

load_dotenv(dotenv_path="/1_python_module/topic17/.env.example")


username = os.getenv('INSTAGRAM_USERNAME')
# username = os.environ.get('INSTAGRAM_USERNAME')
password = os.getenv('INSTAGRAM_PASSWORD')

print(username)
print(password)


# username1 = os.getenv('INSTAGRAM_USERNAME1')
# username = os.environ.get('INSTAGRAM_USERNAME')
# password1 = os.getenv('INSTAGRAM_PASSWORD1')
#
# print(username1)
# print(password1)

inst = Instagram()

inst.sign_in(username, password)

