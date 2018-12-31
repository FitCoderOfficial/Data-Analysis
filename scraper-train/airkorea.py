import urllib.request as req 
from bs4 import BeautifulSoup as bs

url = "https://www.airkorea.or.kr/web"
res = req.urlopen(url)
soup = bs(res, "html.parser")

air = soup.select("myArea10008Val").string

print(air)
