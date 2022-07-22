import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01/'

response = requests.get(URL)

# print(response.status_code)
# print(response.text)

# response = requests.get('http://httpbin.org/get')

# print(response.status_code)
# print(response.text)

# params = {'data1':'data1', 'data2':'data2'}
# headers = {'Content-Type':'application/json; charset=utf-8', 'test' :'test'}
# data = {'data1':'data1', 'data2':'data2'}
# response = requests.post(URL, params= params, headers= headers, data=data)

print(response.status_code)
print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
result = soup.find("title") ##title 태그 찾기
# print(result)
print(result.text)

result2 = soup.find("p") #가장 상단의 태그 하나
result3 = soup.find_all("p",limit = 2) #일치하는 모든 태그, 최대 갯수
print(result2.text)
print(result3)

##class가 tablehead인 것
result4 = soup.find("th", class_= "tablehead") #이름
soup.find("th", attrs={"class":"tablehead"}) 
soup.find("h1", attrs={"title":"welcome"})
soup.find(id="hello")
print(result4.text)