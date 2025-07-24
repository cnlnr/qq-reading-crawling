from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://book.qq.com/")
    page.click('p.unlogin.ypc-link')
    input("登录完成后按回车继续...")
    context.storage_state(path="browser_cache.json")
