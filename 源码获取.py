import requests, json
from selectolax.parser import HTMLParser
from pathlib import Path

cid = 51
bid = "34895175"
parser = HTMLParser(requests.get(f"https://book.qq.com/book-read/{bid}/{cid}", cookies={c['name']: c['value'] for c in json.load(open("cookies.json", encoding="utf-8"))['cookies']}).text)

# 获取书名并创建目录
book_name = parser.css_first('a.book-title').text()
book_path = Path("dataset", f"{book_name}_{bid}")
book_path.mkdir(parents=True, exist_ok=True)

# 获取章节名
chapter_name = parser.css_first('meta[name="keywords"]').attributes.get('content')[len(book_name)+1:]

# 获取正文并保存
open(book_path/f"{chapter_name}.html", "w", encoding="utf-8").write(parser.css_first('div#article').html[85:-6])
