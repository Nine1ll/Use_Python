import smtplib
import datetime


# 구글이 더 이상 지원하지 않음..
my_email = "test.devnine1@gmail.com"
password = "!qwerty2@"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="kgy1607@gmail.com", msg="Hello")
connection.close()
