import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
import time
from pprint import pprint




NUMBER_OF_COLUMNS_TO_SCRAPE = 1 #MAX four only.
WEBSITE = 'https://www.shabdkosh.com'
OUTPUT_FILE = 'shabdkosh_exp_output.json'

headers = {
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
           'Accept-Encoding': 'gzip, deflate, br',
           'Cache-Control': 'max-age=0'}


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
    print(word, link)

    req = requests.get(link, headers=headers)
    con = req.content
    time.sleep(0.3)
    meanings = list()
    soup_meaning = BeautifulSoup(con, 'html.parser')
    meaning_ol_list = soup_meaning.find_all('ol', {'class': 'eirol'})

    for meaning_ol in meaning_ol_list:
        li_tags = meaning_ol.find_all('li')
        meanings.extend([li_tag.find('a').get_text(strip=True) for li_tag in li_tags])
    meanings_dict.update({word: meanings})

pprint(meanings_dict)

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(meanings_dict, f)



