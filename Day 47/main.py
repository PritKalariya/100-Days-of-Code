import requests
from bs4 import BeautifulSoup as BS
import lxml
import smtplib
import os
from dotenv import load_dotenv
import babel.numbers


load_dotenv()
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
DESIRED_PRICE = 15000.00
PRODUCT_URL = "https://www.amazon.in/Oppo-Curved-AMOLED-Screen-Battery/dp/B08HK4QNXM/ref=sr_1_2?dchild=1&keywords=oppo+smart+watch&qid=1620841974&sr=8-2"
HEADERS = {
    "Accept_Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}


# Making request
response = requests.get(url=PRODUCT_URL, headers=HEADERS)
# print(response.status_code)


# Get item title and price
soup = BS(response.content, "lxml")

product_title = soup.find(id="productTitle").get_text().strip()
product_price = soup.find(id="priceblock_ourprice").get_text()
# print(product_title)
# print(product_price)


# Convert the price to float
price_without_symbol = (product_price[1:].split(","))
final_price = ""
for i in price_without_symbol:
    final_price += i
price_as_float = float(final_price)


# Check with desired price and send email
message = f"{product_title} is now available at price " + babel.numbers.format_currency(price_as_float, "INR", locale='as_IN')

if price_as_float <= DESIRED_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = MY_EMAIL,
            msg = f"Subject:Amazon Price Alert!!\n\n{message}\n{PRODUCT_URL}"
        )
    print("Mail sent successfully!")