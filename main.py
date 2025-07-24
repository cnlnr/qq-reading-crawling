from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    browser = p.firefox.launch(headless=True)
    context = browser.new_context(storage_state="browser_cache.json")
    page = context.new_page()
    page.goto("https://book.qq.com/book-read/34895175/51")
    html_content = page.content()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    