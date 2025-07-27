import requests, json
from selectolax.parser import HTMLParser
from pathlib import Path
import re

def crawl_chapter(cid: int, bid: int) -> bool:
    """获取QQ阅读章节内容
    
    Args:
        cid: 章节ID
        bid: 书籍ID
        
    Returns:
        bool: False 返回最后章节
    """

    parser = HTMLParser(requests.get(f"https://book.qq.com/book-read/{bid}/{cid}", cookies={c['name']: c['value'] for c in json.load(open("cookies.json", encoding="utf-8"))['cookies']}).text)

    # 获取书名并创建目录
    book_name = parser.css_first('a.book-title').text()
    book_path = Path("dataset", f"{book_name}_{bid}")
    book_path.mkdir(parents=True, exist_ok=True)

    # 获取章节名
    book_name = re.sub(r'[<>"/\\|:*?]', '_', parser.css_first('a.book-title').text())
    chapter_name = re.sub(r'[<>"/\\|:*?]', '_', parser.css_first('meta[name="keywords"]').attributes.get('content')[len(parser.css_first('a.book-title').text())+1:])
    open(book_path/f"{cid}_{chapter_name}.html", "w", encoding="utf-8").write(parser.css_first('div#article').html[85:-6])

    # 检查是否是最后一章
    div_book_end = parser.css_first('div.book-end.ypc-column-name')
    if div_book_end:
        return False

if __name__ == "__main__":
    crawl_chapter(15, 27612417)
