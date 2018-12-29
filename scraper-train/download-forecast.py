import urllib.request
import urllib.parse

#매개변수를 URL 인코딩 
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId': '108'
}
#요청전용 URL 생성
params = urllib.parse.urlencode(values)
url = API + "?" + params
print("url=", url)


#인코딩한 URL을 읽는 작업
data = urllib.request.urlopen(url)
res = data.read()
text = res.decode("utf-8")

print(text)