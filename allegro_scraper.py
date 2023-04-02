from send_email_func import send_email
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

browser = webdriver.Firefox(
    executable_path=R"C:\Users\barto\InstaPy\assets\geckodriver.exe")
browser.implicitly_wait(5)

browser.get('https://allegro.pl/?source=allegro.com')


sleep(2)
browser.find_element(
    by='xpath', value='//*[@id="opbox-gdpr-consents-modal"]/div/div[2]/div/div[2]/button[1]').click()

sleep(2)
search_box = browser.find_element(
    by='xpath', value="/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div/div[3]/header/div[1]/div/div/div/form/input")

search_box.send_keys("alpha spirit wild fish 12kg")

search_button = browser.find_element(
    by='xpath', value='/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div/div[3]/header/div[1]/div/div/div/form/button')
search_button.click()

select = Select(browser.find_element(value="allegro.listing.sort"))

# select by value
select.select_by_value('p')

sleep(4)

browser.save_full_page_screenshot("karmy.png")

send_email()
