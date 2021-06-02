from bs4 import BeautifulSoup as BS
import requests
from selenium import webdriver
import time


####### Scrape the website for all the necessary data
HEADERS = {
    "Accept_Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

response = requests.get(
    url="https://www.zillow.com/atlanta-ga/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Atlanta%2C%20GA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-84.75034268457031%2C%22east%22%3A-84.21063931542969%2C%22south%22%3A33.59939951688109%2C%22north%22%3A33.934237465267934%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A37211%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A604199%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A2000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D",
    headers=HEADERS
)

data = response.text
soup = BS(data, "html.parser")


all_link_elements = soup.select(".list-card-top a")
all_address_elements = soup.select(".list-card-info address")
all_price_elements = soup.select(".list-card-heading")


all_links = []
for link in all_link_elements:
    href = link["href"]
    # print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)
# print(all_links)


all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]
# print(all_addresses)


all_prices = []
for element in all_price_elements:
    try:
        # Price with only one listing
        price = element.select(".list-card-price")[0].contents[0]
    except IndexError:
        try:
            print('Multiple listings for the card')
            # Price with multiple listings
            price = element.select(".list-card-details li")[0].contents[0]
        except IndexError:
            pass
    finally:
        all_prices.append(price)
# print(all_prices)



####### Create spreadsheet using google form
CHROME_DRIVER_PATH = "YOUR DRIVER PATH"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)


for n in range(len(all_links)):
    driver.get("YOUR FORM LINK")

    time.sleep(5)
    address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_btn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_btn.click()

driver.quit()