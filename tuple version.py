from bs4 import BeautifulSoup
import requests

# Get the HTML content of the Hacker News front page
response = requests.get("https://news.ycombinator.com/news")
yc_web = response.text

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(yc_web, "html.parser")

# Get all article title links and upvote tags
article_tags = soup.select(".titleline > a")
upvote_tags = soup.select(".score")

# Store each article as a tuple: (title, link, upvotes)
articles = []

for tag, upvote_tag in zip(article_tags, upvote_tags):
    article_title = tag.getText()
    article_link = tag.get("href")
    upvotes = int(upvote_tag.text.split()[0])
    articles.append((article_title, article_link, upvotes))

# Find the article with the highest upvotes
most_upvoted = max(articles, key=lambda x: x[2]) #Compare all the articles by their third value (the number of upvotes), and give me the one with the most.”

# Print the result
print("\n-------------------")
print(f"Title: {most_upvoted[0]}")
print(f"Link: {most_upvoted[1]}")
print(f"Upvotes: {most_upvoted[2]}")
print("-----------------------")
