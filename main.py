import requests
from fake_useragent import UserAgent

ua = UserAgent()

# headers = {
#     "User-Agent": ua.random,
#     "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
# }
# url = 'https://httpbin.org/headers'


# query = {
#     "search_query" : "весна"
# }

# r = requests.get('https://httpbin.org/get', headers=headers)
# r = requests.get('https://www.youtube.com/results', headers=headers, params=query)

# print(r.status_code)
# print(r.headers)
# print(r.content)
# print(r.text)
# print(r.json())

# data = {
#     "comments": "ddfdfdfdfdfd lollo",
#     "custemail": "lonn@gjj.com",
#     "custname": "Jonn",
#     "custtel": "2020327",
#
# }
#
# r = requests.post('https://httpbin.org/post', headers=headers, data=data)
# print(r.json()['form']['custemail'])
def get_name(file_url):
    return file_url.split('/')[-1]

url = 'https://image.shutterstock.com/image-photo/blue-viper-snake-closeup-face-600w-1708408498.jpg'

# r = requests.get(url, headers=headers, stream = True)


# with open('1.jpg', 'wb') as fd:
#     for chunk in r.iter_content(chunk_size=1024*10):
#         fd.write(chunk)
#         print('Write chung 100 kb')

r = requests.get(url, headers = {"User-Agent" : ua.random })
with open (get_name(url), 'wb') as fd:
    fd.write(r.content)

