from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
article_texts = [article.getText() for article in articles]
article_links = [article.get("href") for article in articles]
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
print(article_upvotes)

inx_highest_score = 0

for i in range(len(article_upvotes)):
    if article_upvotes[i] > article_upvotes[inx_highest_score]:
        inx_highest_score = i

print(inx_highest_score)



















# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.name)  # name of this tag -> title
# # print(soup.title.string)
# # print(soup.prettify())
#
# # print(soup.a)  # the first anchor tag in the website
# # print(soup.p)
#
# # what if we want all the p tag?
# all_anchor_tags = soup.find_all(name='a')
# # print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#     # print(tag.getText())  # only text
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")  # class is reserved name
# print(f"section_heading:{section_heading.text}")
# print(f"section_heading:{section_heading.get('class')}")
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")  # to select on the id
# print(name)
#
# headings = soup.select(".heading")
# print(headings)


