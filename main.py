import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
}

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

url = 'https://ak.picdn.net/shutterstock/videos/24591794/preview/stock-footage--k-cinemagraph-seamless-loop-portrait-of-caucasian-male-american-football-player-with-a-ball-in.webm'

r = requests.get(url, headers=headers, stream = True)
# print (r.text)
# print(r.content)
# print(r.raw.read(10))

with open('1.webm', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=1024*100):
        fd.write(chunk)
        print('Write chung 100 kb')