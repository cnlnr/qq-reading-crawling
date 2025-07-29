from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    context = p.firefox.launch(headless=False).new_context()
    page = context.new_page()
    page.goto("https://book.qq.com/user-center")
    input("登录完成后按回车继续...")
    context.storage_state(path="cookies.json")
