from bs4 import BeautifulSoup
import requests

# Get the HTML content of the Hacker News front page
response = requests.get("https://news.ycombinator.com/news")
yc_web = response.text

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(yc_web, "html.parser")

# Select all article title links (first anchor tag inside the titleline class)
'''
.titleline – Find any element with the class titleline
> – Direct child selector: only look for children that are directly inside the .titleline element (not nested deeper)
a – The <a> tag (anchor tag, used for links) '''
article_tags = soup.select(".titleline > a")

# Get all the upvote elements associated with articles
upvote_tags = soup.select(".score")


# for n in range(len(article_tags)):
#     tag = article_tags[n]
#     article_title = tag.getText()
#     article_link = tag.get("href")
#     article_upvote = upvote_tags[n].text
#     upvotes.append(article_upvote)
#     upvote_ints = int(upvotes[n].split()[0])# [0] selects the first item from the list -> ["161", "points"][0] -> "161"
#     ints.append(upvote_ints)
#
#
# print(upvotes)
# print(max(ints))
# Extract article titles, links, and upvotes
upvotes = []
title = []
link = []

for tag, upvote_tag in zip(article_tags, upvote_tags):
    article_title = tag.getText()
    title.append(article_title)
    article_link = tag.get("href")
    link.append(article_link)
    upvote = int(upvote_tag.text.split()[0])# [0] selects the first item from the list -> ["161", "points"][0] -> "161"
    upvotes.append(upvote)
    # print(f'\n->article_title: {article_title}')
    # print(f'->article_link: {article_link}')
    # print(f'->article_upvote: {upvote}')
    # print("-----------------------")

# print(upvotes)
# print(title)
# print(link)

most_upvotes = max(upvotes)
# print(most_upvotes)

index = upvotes.index(most_upvotes)
# print(index)

print(f"-------------------\n{title[index]} \n{link[index]}\n{upvotes[index]}\n-----------------------")





# ---------------------LESSON---------------------
# score_tag = soup.find_all(class_="score")
# # print(score_tag)
#
# for tag in score_tag:
#     print(tag.text)


# with open('website.html') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.a)
# # print(soup.li)
# # print(soup.p)
# # print(soup.ul)
#
# all_anchor_tags = (soup.find_all(name="a"))
# # print(all_anchor_tags)
# # print(soup.find_all(name="p"))
#
#
# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))
# #
# # heading = soup.find_all(name="h1", id="name")
# # print(heading)
#
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText())
# # print(section_heading.name)
# # print(section_heading.get("class"))
#
# # company_url = soup.select_one(selector="p a")
# # print(company_url)
# # name = soup.select_one(selector="#name")
# # print(name)
#
# heading = soup.select(".heading")
# print(heading)