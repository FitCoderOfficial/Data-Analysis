from bs4 import BeautifulSoup as bs4 
import urllib.request as req 

url = "http://info.finance.naver.com/marketindex"
res = req.urlopen(url) 

soup = bs4(res, "html.parser")

price_usd = soup.select("div.head_info > span.value")[0].string
price_jpy = soup.select("div.head_info > span.value")[1].string
price_eur = soup.select("div.head_info > span.value")[2].string
price_cny = soup.select("div.head_info > span.value")[3].string
#price_jpy = soup.select_one("#exchangeList > li.on > a.head.jpy > div > span.value").string
#exchangeList > li.on > a.head.jpy > div > span.value

print("UED =", price_usd)
print("JPY =", price_jpy)
print("EUR =", price_eur)
print("CNY =", price_cny)