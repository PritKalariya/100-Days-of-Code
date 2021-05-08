from bs4 import BeautifulSoup as BS
import requests


#Alternative parsing module
# import lxml

# with open("website.html") as file:
#         contents = file.read()

#This is how you make soup
# soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.string)

# Prettify will add indentation to the soup.
# print(soup)
# print(soup.prettify())

# You can access the first tag of any kind by using .p or .a or .h1 etc.
# print(soup.p)

# You can create a list of all occurances of tag with find_all()
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    #getText() gets the text in the tag.
    # print(tag.getText())
    # get() can get the value of any tag attribute.
    # print(tag.get("href"))

# find() works like find_all() but just gets the first occurance.
# You can also find by id.
# heading = soup.find(name="h1", id="name")
# print(heading)

#You can also find by class_ name.
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))

#You can also find by using a CSS Selector:
# print(soup.select_one(selector=".company a"))
# print(soup.select("a"))


##############Scraping Hacker News##############

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BS(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)

    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])