# ---------------------LESSON---------------------
# score_tag = soup.find_all(class_="score")
# # print(score_tag)
#
# for tag in score_tag:
#     print(tag.text)
#
#
# with open('website.html') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
# print(soup.li)
# print(soup.p)
# print(soup.ul)
#
# all_anchor_tags = (soup.find_all(name="a"))
# print(all_anchor_tags)
# print(soup.find_all(name="p"))
#
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find_all(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
# name = soup.select_one(selector="#name")
# print(name)
#
# heading = soup.select(".heading")
# print(heading)