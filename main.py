from playwright.sync_api import sync_playwright
import json


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # 加载 cookies
        with open("cookies.json", "r", encoding="utf-8") as f:
            cookies = json.load(f)
        context.add_cookies(cookies)

        page = context.new_page()
        page.goto("https://book.qq.com/")

        # 加载 localStorage
        with open("localStorage.json", "r", encoding="utf-8") as f:
            local_storage = json.load(f)
        for key, value in local_storage.items():
            page.evaluate(f"localStorage.setItem('{key}', '{value}')")

        # 刷新页面以应用缓存
        page.reload()

        print("已加载缓存并保持登录状态！")
        # 访问指定页面
        page.goto("https://book.qq.com/book-read/34895175/65")
        print("已访问目标页面！")

        # 获取页面内容的索引
        content = page.content()
        print("页面内容索引：")
        print(content)

        # 关闭浏览器
        browser.close()


if __name__ == "__main__":
    main()
