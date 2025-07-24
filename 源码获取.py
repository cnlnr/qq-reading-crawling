import requests
import json

url = "https://book.qq.com/book-read/34895175/51"

# 加载缓存数据
with open("browser_cache.json", "r", encoding="utf-8") as f:
    storage = json.load(f)
cookies = {cookie['name']: cookie['value'] for cookie in storage['cookies']}

# 发起请求
response = requests.get(url, cookies=cookies)

# 保存页面内容
with open("index.html", "w", encoding="utf-8") as f:
    f.write(response.text)
