import requests
from datetime import datetime
import smtplib
import urllib3
import time
urllib3.disable_warnings()

MY_EMAIL = "@gmail.com"
MY_PASSWORD = "adcd1234()"
MY_LAT = 37.566536
MY_LONG = 126.977966


def is_iss_near(iss_la, iss_long):
    if MY_LAT-5 <= iss_la <= MY_LAT+5 and MY_LONG-5 <= iss_long <= MY_LONG+5:
        return True
    return False

def is_dark(now, s_rise, s_set):
    if s_rise<= now <=s_set:
        return False
    return True

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour
while True:
    time.sleep(60)
    if is_iss_near(iss_latitude, iss_longitude) and is_dark(time_now, sunrise, sunset):
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look up👆\n\nThe ISS is above you in the sky"
        )

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



