# alt+enter
import requests
# url = "https://httpbin.org/image/jpeg"
url = "https://httpbin.org/post"
response = requests.post(url)
print(response)
print(response.content)

path_to_download = "/home/ulan/edu/justcode/python14/topic14/test_img.jpg"

with open(path_to_download, 'wb') as file:
    file.write(response.content)







