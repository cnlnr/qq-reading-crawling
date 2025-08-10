import requests, json
from pathlib import Path

# 获取指定章节
def 标题_内容(bid, cid, cookies):
    阅读_数据 = requests.get(f'https://ubook.reader.qq.com/api/book/read?bid={bid}&cid={cid}', cookies=cookies).json()['data']
    标题 = 阅读_数据.get('title')
    内容 = 阅读_数据.get('content')
    return 标题, 内容



# 获取书名和总章节数
def 详细(bid, cookies):
    详细 = requests.get(f'https://ubook.reader.qq.com/api/book/detail?bid={bid}', cookies=cookies).json()['data']['book']
    书名 = 详细['title']
    总章节数 = 详细['totalChapters']
    return 书名, 总章节数

def cookies(json_path):
    return {c['name']: c['value'] for c in json.load(open(json_path))['cookies']}





def 遍历章节(bid, cookies):
    # 获取书名和总章节数
    书名, 总章节数 = 详细(bid, cookies)
    # 遍历章节
    for cid in range(1, 总章节数 + 1):
        # 获取章节标题和内容
        标题, 内容 = 标题_内容(bid, cid, cookies)
        # 处理非法文件名
        def 过滤文件名(名字):
            # 移除文件名中不允许的字符
            not法字符 = '<>:"/\\|?*'
            for 字符 in not法字符:
                名字 = 名字.replace(字符, '')
            return 名字.strip()

        文件名_书名 = 过滤文件名(书名)
        文件名_标题 = 过滤文件名(标题)
        # 保存正文
        书_路径 = Path(f"dataset/{文件名_书名}_{bid}")
        书_路径.mkdir(parents=True, exist_ok=True)
        # 保存文件
        Path(f"{书_路径}/{cid}_{文件名_标题}.html").write_text(内容, encoding='utf-8')
        print(f'\r\033[K{cid} {文件名_标题}', end='')






if __name__ == "__main__":
    遍历章节(38128522, cookies('cookies.json'))
    print('\r\033[K完成')
