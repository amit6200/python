import requests
from bs4 import BeautifulSoup
data=requests.get("https://www.youtube.com/watch?v=R2G7xQymBCs")
# print(data.content)
soup=BeautifulSoup(data.content,features="html.parser")
print(soup.html.head.title)