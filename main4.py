from bs4 import BeautifulSoup
import re

# soup1 = BeautifulSoup (html_doc, 'html.parser')
# soup2 = BeautifulSoup (html_doc, 'lxml')

with open('html4/page.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

# print(soup)
# title = soup.title
# print(title)
# print(title.name)
# print(title.attrs)
# print(title.text)
# print(title.get_text())
# print(title.string)

h1 = soup.h1
# print(h1)
# print(h1.attrs)
# print(h1.attrs['id'])
# print(h1['id'])
# print(h1.get('id'))
# print(h1.has_attr('id'))
# print(h1.get_text(strip=True, separator=' '))

#find() find_all()
# print(soup.a)
# print(soup.find('nav').find('a').get('href'))

# links = soup.find('nav').find_all('a')
# print(len(links))
# for link in links:
#     print(f'{link.get_text(strip=True)} - {link.get("href")}')
# links = soup.find('nav').find_all('a', class_='p-2')
# links = soup.find('nav').find_all('a', class_='p-2 link-secondary')
# links = soup.find('nav').find_all('a', { 'class' : 'p-2 link-secondary'})
# links = soup.find('nav').find_all('a',attrs =  { 'class' : 'p-2', "data-link" : "link"})
# links = soup.find('nav').find_all('a',attrs =  { 'id' : 'design'})
# links = soup.find('nav').find_all(id = 'design')
# print(links)

# print(soup.find_all(['h1', 'h2', 'h3']))
