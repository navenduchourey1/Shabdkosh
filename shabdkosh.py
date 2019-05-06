import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
from pprint import pprint

NUMBER_OF_COLUMNS_TO_SCRAPE = 1 #MAX four only.
WEBSITE = 'https://www.shabdkosh.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

r = requests.get('https://www.shabdkosh.com/browse/english-hindi/S', headers=headers)
c=r.content
soup=BeautifulSoup(c,'html.parser')

words_div = soup.find('h2', text='Words').parent
container_div = words_div.find('div', {'class': 'container'})

word_columns = container_div.find_all('div', {'class': 'col-sm'})
words = dict()

max_word_index = NUMBER_OF_COLUMNS_TO_SCRAPE - 1


for word_index, word_column in enumerate(word_columns):
    word_links = {a.get_text(strip=True): urljoin(WEBSITE, a['href']) for a in word_column.find_all('a')}
    words.update(word_links)

    if word_index == max_word_index:
        break

meanings_dict = {}

for word, link in words.items():
    #print(word, link)

    req = requests.get(link, headers=headers)
    con = req.content

    meanings = list()
    soup_meaning = BeautifulSoup(con, 'html.parser')
    meaning_ol_list = soup_meaning.find_all('ol', {'class':'wnol'})

    for meaning_ol in meaning_ol_list:
        meanings.extend([li.get_text(strip=True) for li in meaning_ol.find_all('li')])

    meanings_dict.update({word: meanings})



#pprint(meanings_dict)



with open('shabdkosh.json', 'w') as f:
    json.dump(meanings_dict, f)

