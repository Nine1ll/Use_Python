import requests
from datetime import datetime
USERNAME = "nine1ll"
TOKEN = "gospotb1607"
GRAPHID = 'graph1'
# Create pixela user
pixela_endpoint = 'https://pixe.la/v1/users'

user_parmas ={
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_parmas)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id': GRAPHID,
    'name': 'Meditate Graph',
    'unit': 'Min',
    'type': 'float',
    'color': 'momiji'

}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)


today = datetime.now()

days_config = {
    'date': today.strftime("%Y%m%d"),
    'quantity': '100'
}
# response = requests.post(url=days_endpoint, json=days_config, headers=headers)
# print(response.text)

# update_days_endpoint = f"{graph_endpoint}/{GRAPHID}/{today.strftime('%Y%m%d')}"
# update_day = {
#     'quantity': '600'
# }
# response = requests.put(url=update_days_endpoint, headers=headers, json=update_day)
# print(response.text)