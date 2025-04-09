from bs4 import BeautifulSoup
import requests
import sys

stdoutOrigin=sys.stdout
sys.stdout = open("log.txt", "w", encoding="utf-8")

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
web = response.text

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(web, "html.parser")

movie_name = soup.find_all(name="h3")


def remove_num(movie_name):
    words = movie_name.split()
    return ' '.join(words[1:])


j = 0
for movie_title in reversed(movie_name):
    j = j + 1
    print(f'{j}) {remove_num(movie_title.text)}')


sys.stdout.close()
sys.stdout = stdoutOrigin