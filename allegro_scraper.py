from send_email_func import send_email
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from time import sleep


options = Options()
options.add_argument("--headless")
browser = webdriver.Firefox(
    executable_path=R"C:\Users\barto\InstaPy\assets\geckodriver.exe", options=options)


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

# get particular offers
offers_list = []
index = 5
for _ in range(10):
    offer_specs = []
    offers_name = browser.find_element(
        by='xpath', value=f'//*[@id="search-results"]/div[5]/div/div/div[1]/div/div/section[2]/article[{index}]/div/div/div[2]/div[1]/h2/a').text

    link_object = browser.find_element(
        by='xpath', value=f'//*[@id="search-results"]/div[5]/div/div/div[1]/div/div/section[2]/article[{index}]/div/div/div[2]/div[1]/h2/a')
    link = link_object.get_attribute("href")

    price = browser.find_element(
        by='xpath', value=f'//*[@id="search-results"]/div[5]/div/div/div[1]/div/div/section[2]/article[{index}]/div/div/div[2]/div[2]/div/div/span').text
    index += 1

    offer_specs.append(offers_name)
    offer_specs.append(link)
    offer_specs.append(price)
    offers_list.append(offer_specs)

print(offers_list)


with open('offers.txt', 'w', encoding="UTF-8") as file:
    file.writelines([str(offer).replace("[", "").replace("]",
                    "") + "\n" for offer in offers_list])


browser.save_full_page_screenshot("karmy.png")


send_email()
print("Email was sent")


browser.quit()
