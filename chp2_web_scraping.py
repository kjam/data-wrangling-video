from __future__ import print_function
import requests
from lxml import html


response = requests.get('http://kjamistan.com')

page = html.fromstring(response.content)

page.make_links_absolute(base_url='http://kjamistan.com')

posts = page.xpath('//article[@class="post"]')
#posts = page.cssselect('article.post')

all_posts = []

for post in posts:
    link = post.xpath('header/h2/a')[0].get('href')
    title = post.xpath('header/h2/a/text()')[0]
    all_posts.append((title, link))

print(all_posts)
