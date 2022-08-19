import requests
import datetime

APP_ID = "10635565"
API_KEY = "69cfceb39e7768a820bc6d8ab30a9644"
EXERCISE_END_POINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_END_POINT = 'https://api.sheety.co/64f6365dbe4f8bc8b3d5837bf0dcf450/myWorkouts/workouts'

GENDER = 'male'
WEIGHT_KG = 72
HEIGHT_CM = 175.1
AGE = 23
TODAY = datetime.datetime.now()
headers = {
    "x-app-id": APP_ID,
    'x-app-key': API_KEY
}
exercise_text = input("Tell me which exercises you did: ")

parameters = {
    'query': exercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

response = requests.post(EXERCISE_END_POINT, headers=headers, json=parameters)
