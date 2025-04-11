from selenium import webdriver
from selenium.webdriver.common.by import By

import schedule
url = "https://orteil.dashnet.org/experiments/cookie/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

cookie = driver.find_element(By.ID,value="cookie")

items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]



all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
item_prices = []

for price in all_prices:
    element_text = price.text
    if element_text != "":
        cost = float(element_text.split("-")[1].strip().replace(",", ""))
        item_prices.append(cost)

# print(item_prices)
# print(item_ids)


def job():
        affordable_upgrades = []
        cookie_count = driver.find_element(By.ID, value="money")
        cookie_cout_int = float(cookie_count.text.replace(",", ""))
        print(cookie_cout_int)
        for i in item_prices:
            if cookie_cout_int > i:
                affordable_upgrades.append(i)
        buy_index = affordable_upgrades.index(max(affordable_upgrades))
        buyID = item_ids[buy_index]
        print(buyID)
        driver.find_element(by=By.ID, value=buyID).click()
schedule.every(10).seconds.do(job)
while True:
    cookie.click()
    schedule.run_pending()



driver.quit()