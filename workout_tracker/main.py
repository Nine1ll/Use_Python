import requests
import datetime
import os

NATURAL_END_POINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

load_dotenv()

os.environ["APP_ID"] = "10635565"
os.environ["APP_KEY"] = "69cfceb39e7768a820bc6d8ab30a9644"
os.environ["SHEET_END_POINT"] = 'https://api.sheety.co/64f6365dbe4f8bc8b3d5837bf0dcf450/myWorkouts/workouts'
os.environ["TOKEN"] = "roqkfdydtltmxpaxhzms"

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("APP_KEY")
SHEET_END_POINT = os.environ["SHEET_END_POINT"]
TOKEN = os.environ["TOKEN"]


GENDER = 'male'
WEIGHT_KG = 72
HEIGHT_CM = 175.1
AGE = 23
TODAY = datetime.datetime.now().strftime('%d/%m/%Y')
TIME_NOW = datetime.datetime.now().strftime('%X')

exercise_text = input("Tell me which exercises you did: ")

natural_headers = {
    "x-app-id": APP_ID,
    'x-app-key': API_KEY
}

natural_parameters = {
    'query': exercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

natural_response = requests.post(url=NATURAL_END_POINT, headers=natural_headers, json=natural_parameters)
natural_result = natural_response.json()
print(natural_result)
for exercise in natural_result["exercises"]:
    bearer_headers = {
        'Authorization': f"Bearer {TOKEN}"
    }
    sheet_parameters = {
        'workout': {
            'date': TODAY,
            'time': TIME_NOW,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    sheet_response = requests.post(url=SHEET_END_POINT, json=sheet_parameters, headers=bearer_headers)
    print(sheet_response.text)
