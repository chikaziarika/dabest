
# importing the modules 
import requests 
from bs4 import BeautifulSoup 
  
# providing url 
URL = "https://www.detik.com/search/searchall?query=banjir&result_type=relevansi&siteid=3"
r = requests.get(URL)
soup = BeautifulSoup(r.content, "html.parser")
results = soup.find_all('article',class_='list-content__item')
# element = soup.find_all('article', {'class':'list-content__item'})
# childEl = element.find_all('list-content__item')
xTitle = []
xSubs = []
for data in results:
    title = data.find('h3', class_="media__title")
    subtitle = data.find('h2', class_="media__subtitle")
    desc = data.find('div', class_='media__desc')
    if title:
        xTitle.append(title.text.strip())
    if subtitle:
        xSubs.append(subtitle.text.strip())
# print(title.text.strip())
# print(subtitle.text.strip())
# print(desc.text.strip())

# print(xTitle)
print(xSubs)
# print(set(th.text for th in element))
