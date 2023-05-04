# #Working with CSV files and Analysing data with Pandas

# ##Challenge 1: Open the weather_data.csv. Use readlines() to create a list named data that contains the value from the .csv file.

# # import csv

# # file = open("weather_data.csv", "r")

# # temperature = []

# # data = list(csv.reader(file, delimiter=","))

# # for row in data:
# #     if row[1] != "temp":
# #         temperature.append(int(row[1]))
# # print(temperature)

# import pandas
# data = pandas.read_csv("weather_data.csv")
# #print(data["temp"])

# data_dict = data.to_dict()
# #print(data_dict)

# temp_list = data["temp"].to_list()
# # print(len(temp_list))

# # print(data["temp"].mean())
# # print(data["temp"].max())

# # #Get Data in Columns
# # print(data["condition"])
# # print(data.condition)

# # #Get Data in Row
# # print(data[data.day == "Monday"].temp)
# # # print(data[data.temp == data.temp.min()].day)

# # celsius_temp = data[data.day == "Monday"].temp

# # fahrenheit_temp = celsius_temp * 9 / 5 + 32

# # print(fahrenheit_temp)


# #Creating a dataframe from scratch

# # data_dict = {
# #     "students": ["Amy", "James", "Angela"],
# #     "scores": [76, 56, 65]
# # }

# # data = pandas.DataFrame(data_dict)
# # # convert dataframe to a CSV file
# # # data.to_csv("new_data.csv")

# create a CSV called squirrel_count that has a small table containing "Fur Color" and "count" column.
# Get a number of how many grey colored squirrels are present, how many cinnamon color and how many black color squirrels.
import csv
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#print(data["Primary Fur Color"])
gray_squirrel_count =  0
cinnamon_squirrel_count = 0
black_squirrel_count = 0

for i in data["Primary Fur Color"]:
    if i == "Gray":
        gray_squirrel_count += 1
    elif i == "Cinnamon":
        cinnamon_squirrel_count += 1
    elif i == "Black":
        black_squirrel_count += 1

print(gray_squirrel_count)
print(cinnamon_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")