KEYWORDS = ['дизайн', 'фото', 'web', 'python']

from bs4 import BeautifulSoup
import requests
import pprint
from Headers import HEADERS



page = requests.get('https://habr.com/ru/rss/all/all/?fl=ru', headers=HEADERS)
soup = BeautifulSoup(page.text, 'html.parser')


posts = soup.find_all('item')
for post in posts:
    post_url = post.guid.string
    post_date = post.pubdate.string
    if not post_url:
        continue
    post_id = int(post_url.split('/')[-2])
    post_date = post_date.split(', ')[-1]

    hubs = post.find_all('category')
    for hub in hubs:
       corrected_hub = hub.string.lower()
       if any([corrected_hub in chosen for chosen in KEYWORDS]):
           title_element = post.find('title')
           print(f"\nDATE : {post_date}, \nTitle: {title_element.text}, \
               \nLINK: {post.guid.string}")
           break
