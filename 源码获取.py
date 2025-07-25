import requests
import json
from selectolax.parser import HTMLParser

url = "https://book.qq.com/book-read/34895175/51"

# 加载缓存数据
with open("browser_cache.json", "r", encoding="utf-8") as f:
    storage = json.load(f)
cookies = {cookie['name']: cookie['value'] for cookie in storage['cookies']}

# 获取源码
html = requests.get(url, cookies=cookies).text

# 获取正文
parser = HTMLParser(html)
div_article = parser.css_first('div#article')
div_article_html = div_article.html[85:][:-6] if div_article else "<p>没有找到正文</p>"

# 保存正文
with open("index.html", "w", encoding="utf-8") as f:
    f.write(div_article_html)
