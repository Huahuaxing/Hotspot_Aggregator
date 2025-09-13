import requests
from bs4 import BeautifulSoup
import sys

def get_douban_top250():
    list = []
    for startNum in range(0, 250, 25):
        url = f"https://movie.douban.com/top250?start={startNum}&filter="
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        allTitles = soup.find_all("span", attrs={"class": "title"})

        for title in allTitles:
            if "/" not in title.string:
                list.append(title.string)

    for ranking, title in enumerate(list, 1):
        print(f"{ranking} {title.string}")


if __name__ == "__main__":
    get_douban_top250()
