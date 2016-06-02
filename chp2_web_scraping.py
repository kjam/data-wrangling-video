from __future__ import print_function
import requests
from lxml import html


response = requests.get('http://www.kdnuggets.com/news/top-stories.html')

page = html.fromstring(response.content)

#top_stories = page.xpath('//div[contains(@class, "post")]/ol/li')
top_stories = page.cssselect('div ol li')

story_list = []

for story in top_stories:
    link = story.xpath('a')[0].get('href')
    story_list.append((story.text_content(), link))

print(story_list)
