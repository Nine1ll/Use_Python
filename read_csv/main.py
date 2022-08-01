# # with open("weather_data.csv") as weather:
# #     datas = weather.readlines()
# #     for data in datas:
# #         data = data.strip()
# #         print(data)
# #
# # import csv
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# #
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # # print(temp_list)
# # # mean 찾기
# # print(round(sum(temp_list) / len(temp_list), 2))
# # print(data["temp"].mean())
# #
# # # max값 찾기
# # print(max(temp_list))
# # print(data["temp"].max())
# #
# # # condition 불러오기
# # data["condition"]
# # data.condition
#
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
#
# # monday = data[data.day == "Monday"]
# # print(monday.temp)
# # fahrenheit = monday.temp*1.8 + 32
# # print(fahrenheit)
#
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = 0
red = 0
black = 0
colors = data["Primary Fur Color"].to_list()
# # 더 효율적인 방법
# gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
# gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])

for color in colors:
    if color == "Gray":
        gray += 1
    elif color == "Cinnamon":
        red += 1
    elif color == "Black":
        black += 1

print(f"gray: {gray}, red: {red}, black: {black}")

sq_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray, red, black]
}

data = pandas.DataFrame(sq_dict)
data.to_csv("squirrel_count")

