import urllib.request as req 
from bs4 import BeautifulSoup as bs4

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

res = req.urlopen(url)
soup = bs4(res, "html.parser")

title = soup.find("title").string
wf = soup.find("wf").string
print(title)
print(wf)