from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://docs.google.com/forms/ your own google forms")
    print(page.title())
    browser.close()

from playwright.sync_api import Playwright, sync_playwright, expect
import time

# 自動化記錄模式
# python -m playwright codegen "https://docs.google.com/forms/ your own google forms"

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://docs.google.com/forms/ your own google forms
    page.goto("https://docs.google.com/forms/ your own google forms")
    print(page.title())
    # Fill input[type="date"]
    page.locator("input[type=\"date\"]").fill("2022-07-26")
    # Press Tab
    page.locator("input[type=\"date\"]").press("Tab")
    # Fill text=發票號碼 *範例：UX-70757527 沒有或者已經登入載具填入 NA您的回答 >> input[type="text"]
    page.locator("text=發票號碼 *範例：UX-70757527 沒有或者已經登入載具填入 NA您的回答 >> input[type=\"text\"]").fill("UT-12345678")
    # Press Tab
    page.locator("text=發票號碼 *範例：UX-70757527 沒有或者已經登入載具填入 NA您的回答 >> input[type=\"text\"]").press("Tab")
    # Press ArrowDown
    page.locator("div[role=\"option\"]:has-text(\"選擇\")").first.press("ArrowDown")
    # Click text=飲食 >> nth=1
    page.locator("text=飲食").nth(1).click()
    time.sleep(0.5)
    # Press Tab
    page.locator(".ry3kXd > div:nth-child(3)").first.press("Tab")
    # Press ArrowDown
    page.locator("div[role=\"option\"]:has-text(\"選擇\")").nth(1).press("ArrowDown")
    # Click text=菜錢 >> nth=1
    page.locator("text=菜錢").nth(1).click()
    time.sleep(0.5)
    # Press Tab
    page.locator("div:nth-child(4) > div > .geS5n > .vQES8d > .jgvuAb > div > .ry3kXd > div:nth-child(3)").press("Tab")
    # Press ArrowDown
    page.locator("div[role=\"option\"]:has-text(\"選擇\")").nth(2).press("ArrowDown")
    # Click text=現金 >> nth=1
    page.locator("text=現金").nth(1).click()
    time.sleep(0.5)
    # Press Tab
    page.locator("div:nth-child(5) > div > .geS5n > .vQES8d > .jgvuAb > div > .ry3kXd > div:nth-child(3)").press("Tab")
    # Fill input[type="text"] >> nth=1
    page.locator("input[type=\"text\"]").nth(1).fill("ASDF125")
    # Press Tab
    page.locator("input[type=\"text\"]").nth(1).press("Tab")
    # Fill text=金額 *您的回答 >> input[type="text"]
    page.locator("text=金額 *您的回答 >> input[type=\"text\"]").fill("123")
    # Press Tab
    page.locator("text=金額 *您的回答 >> input[type=\"text\"]").press("Tab")
    # Press Enter
    page.locator("div[role=\"button\"]:has-text(\"提交\")").press("Enter")
    page.wait_for_url("https://docs.google.com/forms/ Thie is the redereact page to your google forms")
    # ---------------------
    print(page.title(), "Insert Complete!")
    context.close()
    browser.close()
    
with sync_playwright() as playwright:
    run(playwright)
