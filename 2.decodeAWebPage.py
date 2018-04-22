import requests
from bs4 import BeautifulSoup
base_url = "https://www.nytimes.com/"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")
# print(soup)
all_p_cn_text_body = soup.select("ul.mini-navigation-menu > li > a")
# all_p_cn_text_body = soup.select("article.story.theme-summary.lede > h2.story-heading > a")
for elem in all_p_cn_text_body:
  print(elem.text)
