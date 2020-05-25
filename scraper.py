import requests
from bs4 import BeautifulSoup


class OffSecSpider:

    results = []
    
    def fetch(self, url):
        return requests.get(url)
    
    def parse(self, html):

        soup = BeautifulSoup(html)

        for head in soup.find_all("h3"):
            try:
                a_tag = head.find("a")
                title = a_tag.get("title")
                link = a_tag.get("href")
                dictionary = {"title":title, 
                              "link":link}
                self.results.append(dictionary)
            except:
                 pass

    

    def run(self):
        response = self.fetch("https://www.offensive-security.com/blog.../")
        self.parse(response.text)
 


if __name__ == '__main__':
    scraper = OffSecSpider()
    scraper.run()    
   