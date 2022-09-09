from playwright.sync_api import Playwright, sync_playwright, expect
import time
# 自動化記錄模式
# python -m playwright codegen "https://"
def date(recieve_date):
    import main_QRCode_01info_layout as Codeinfo
    date_year=int(recieve_date[0:3])+1911
    date_month_str=recieve_date[3:5]
    date_date_str=recieve_date[5:7]
    date=f'{date_year}-{date_month_str}-{date_date_str}'
    print(date)
    return date, bool

def recieve_num(recieve):
    import main_QRCode_01info_layout as Codeinfo
    recieve=f'{recieve[0:2]}-{recieve[2:]}'
    print(recieve)
    return recieve

def recieve_class():
    pass

def recieve_gen():
    pass

def pay_method():
    pass

def item_list():
    import main_QRCode_03_reform as reform
    return reform.wks_data_match()

def totle_cost(recieve_total_sale):
    import main_QRCode_01info_layout as Codeinfo
    cost_str=recieve_total_sale
    cost=str(int(cost_str))
    print(cost)
    return cost

def run(playwright: Playwright) -> None:
    # data build
    time.sleep(0.5)
    recieve_date=date(recieve_date)
    recieve=recieve_num(recieve)
    recieve_total_sale=totle_cost(recieve_total_sale)
    # start
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://
    # Create your own google forms with several blank answer.
    page.goto("https://docs.google.com/forms/d/e/1FAIpQLSfqGV5LsRl3QI7FMwUoQpW0C2lHsPDYiehziqQ2OaYCxOh3AA/viewform")
    print(page.title())

    page.locator("input[type=\"date\"]").fill(recieve_date)
    page.locator("input[type=\"date\"]").press("Tab")
    page.locator("text=發票號碼 *範例：UX-70757527 沒有或者已經登入載具填入 NA您的回答 >> input[type=\"text\"]").fill(recieve)
    # ----------Press Tab----------
    page.locator("text=發票號碼 *範例：UX-70757527 沒有或者已經登入載具填入 NA您的回答 >> input[type=\"text\"]").press("Tab")
    page.locator("div[role=\"option\"]:has-text(\"選擇\")").first.press("ArrowDown")
    page.locator("text=飲食").nth(1).click()
    time.sleep(0.5)
    # ----------Press Tab----------
    page.locator(".ry3kXd > div:nth-child(3)").first.press("Tab")
    page.locator("div[role=\"option\"]:has-text(\"選擇\")").nth(1).press("ArrowDown")
    page.locator("text=菜錢").nth(1).click()
    time.sleep(0.5)
    # ----------Press Tab----------
    page.locator("div:nth-child(4) > div > .geS5n > .vQES8d > .jgvuAb > div > .ry3kXd > div:nth-child(3)").press("Tab")
    page.locator("div[role=\"option\"]:has-text(\"選擇\")").nth(2).press("ArrowDown")
    page.locator("text=現金").nth(1).click()
    time.sleep(0.5)
    page.locator("div:nth-child(5) > div > .geS5n > .vQES8d > .jgvuAb > div > .ry3kXd > div:nth-child(3)").press("Tab")
    page.locator("input[type=\"text\"]").nth(1).fill(item_list())
    page.locator("input[type=\"text\"]").nth(1).press("Tab")
    page.locator("text=金額 *您的回答 >> input[type=\"text\"]").fill(recieve_total_sale)
    # ----------Press Tab----------
    page.locator("text=金額 *您的回答 >> input[type=\"text\"]").press("Tab")
    page.locator("div[role=\"button\"]:has-text(\"提交\")").press("Enter")
    page.wait_for_url("https://docs.google.com/forms/d/e/1FAIpQLScowkYbZ9aVeCT5lYTDiuoTf12PnnpgrGT6i8OxBaVHvn3YIA/formResponse")
    # ---------------------

    print(page.title(), "Insert Complete!")
    # context.close()
    # browser.close()

# with sync_playwright() as playwright:
#     run(playwright)
