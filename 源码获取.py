import requests, json
from selectolax.parser import HTMLParser

cookies = {c['name']: c['value'] for c in json.load(open("cookies.json", encoding="utf-8"))['cookies']}
html = requests.get("https://book.qq.com/book-read/34895175/51", cookies=cookies).text
parser = HTMLParser(html).css_first('div#article')
div_article = parser.html[85:-6] if parser else "<p>没有找到正文</p>"
open("index.html", "w", encoding="utf-8").write(div_article)
