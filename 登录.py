from playwright.sync_api import sync_playwright
import json
import time


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        page = context.new_page()
        page.goto("https://book.qq.com/")

        # 隐藏 webdriver 痕迹
        page.evaluate(
            "() => { Object.defineProperty(navigator, 'webdriver', {get: () => undefined}); }")

        print("请登录，操作完成后手动关闭浏览器窗口，然后回到命令行按回车继续...")
        input("按回车键继续：")
        # 保存 cookies
        cookies = context.cookies()
        with open("cookies.json", "w", encoding="utf-8") as f:
            json.dump(cookies, f, ensure_ascii=False, indent=2)

        # 保存 localStorage
        local_storage = page.evaluate(
            "() => { let s = {}; for (let i = 0; i < localStorage.length; i++) { let k = localStorage.key(i); s[k] = localStorage.getItem(k); } return s; }"
        )
        with open("localStorage.json", "w", encoding="utf-8") as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=2)

        print("缓存数据已保存为 cookies.json 和 localStorage.json")


if __name__ == "__main__":
    main()
