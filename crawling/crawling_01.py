from urllib import response
import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01/'

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
##q1
# result1 = soup.find(id="cook")
# print(result1.text)

##q2
# table = []

# key = []
# elements = soup.find("table").find_all('th')
# for element in elements:
#     key.append(element.text)


# values = soup.find("table").find('tbody').find_all('tr')
# for value in values:
#     temp_value = []
#     for td_values in value.find_all("td"):
#         temp_value.append(td_values.text)
#     table.append(dict(zip(key, temp_value)))

# print(table)

##q3 

for t in soup.find_all("a"):
    response = requests.get('https://crawlingstudy-dd3c9.web.app/01/'+ t.attrs['href' ])
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.find('p').text.strip())

