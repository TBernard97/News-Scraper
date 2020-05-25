from bs4 import BeautifulSoup
import requests

request = requests.get("https://www.offensive-security.com/blog.../")

soup = BeautifulSoup(request.text)

for head in soup.find_all("h3"):
    try:
        a_tag = head.find("a")
        title = a_tag.get("title")
        link = a_tag.get("href")
        print(link)
    except:
        pass