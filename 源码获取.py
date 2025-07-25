from selectolax.parser import HTMLParser
import requests
import json

url = "https://book.qq.com/book-read/34895175/51"

# 加载cookie
with open("browser_cache.json", "r", encoding="utf-8") as f:
    storage = json.load(f)
cookies = {cookie['name']: cookie['value'] for cookie in storage['cookies']}

# 获取页面
html = requests.get(url, cookies=cookies).text
parser = HTMLParser(html)

# 获取div#article内部内容
div_article = parser.css_first('div#article')
if div_article:
    inner_html = ""
    for node in div_article.iter(include_text=True):
        if node != div_article:
            inner_html += node.html
else:
    inner_html = ""

# 保存结果
with open("index.html", "w", encoding="utf-8") as f:
    f.write(inner_html)
