import requests, json

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

