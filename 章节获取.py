import requests, json
from pathlib import Path

# 获取指定章节
def read(bid, cid, cookies):
    read_data = requests.get(f'https://ubook.reader.qq.com/api/book/read?bid={bid}&cid={cid}', cookies=cookies).json()['data']
    title = read_data.get('title')
    content = read_data.get('content')
    return title, content

# 获取书名和总章节数
def detail(bid, cookies):
    book_detail = requests.get(f'https://ubook.reader.qq.com/api/book/detail?bid={bid}', cookies=cookies).json()['data']['book']
    book_title = book_detail['title']
    totalChapters = book_detail['totalChapters']
    return book_title, totalChapters

def cookies(json_path):
    return {c['name']: c['value'] for c in json.load(open(json_path))['cookies']}

# 遍历章节
def traverse_chapters(bid, cookies):
    # 获取书名和总章节数
    book_title, totalChapters = detail(bid, cookies)
    # 遍历章节
    for cid in range(1, totalChapters + 1):
        # 获取章节标题和内容
        title, content = read(bid, cid, cookies)
        # 保存正文
        book_path = Path(f"dataset/{book_title}_{bid}")
        book_path.mkdir(parents=True, exist_ok=True)
        # 保存文件
        Path(f"{book_path}/{cid}_{title}.html").write_text(content, encoding='utf-8')
        print(f'{cid} {title}', end='\r')


if __name__ == "__main__":
    traverse_chapters(656352, cookies('cookies.json'))
    print('完成')
