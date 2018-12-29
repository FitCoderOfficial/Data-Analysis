import sys
import urllib.request as req
import urllib.parse as parse 

if len(sys.argv) <= 1:
    print("USAGE: doenload-forecast-argv <Region Number>")
    sys.exit()
regionNumber = sys.argv[1] 

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId': regionNumber
}
#요청전용 URL 생성
params = parse.urlencode(values)
url = API + "?" + params
print("url=", url)

#인코딩한 URL을 읽는 작업
data = req.urlopen(url)
res = data.read()
text = res.decode("utf-8")

print(text)