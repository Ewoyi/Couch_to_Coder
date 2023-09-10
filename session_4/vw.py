# BASE TASK
import csv
from collections import namedtuple

Car = namedtuple("Car", "model year price transmission mileage fuelType tax mpg engineSize")
cars = []

with open("vw-2.csv", "r") as csv_file:
    reader = csv.reader(csv_file, skipinitialspace=True)
    next(reader)
    for row in reader:
        new_car = Car(*row)
        cars.append(new_car)
# print(cars)

# TASK 1
most_expensive_cars = cars[0]

for car in cars:
    if(int(car.price) > int(most_expensive_cars.price)):
        most_expensive_cars = car
print(most_expensive_cars.model)
print(most_expensive_cars.price)

# TASK 2
total_price = 0

for car in cars:
    if(car.model == "Golf"):
        total_price += int(car.price)
        average_price = total_price/len(car)
print(average_price)

# TASK 3
total_mileage = 0

for car in cars:
    if(car.model == "Polo"):
        total_mileage += int(car.mileage)
        average_mileage = total_mileage/len(car)
print(average_mileage)

# EXTENSION
import pandas as pd
import matplotlib.pyplot as plt

vw = pd.read_csv("vw-2.csv")
# print(vw)

# TASK 4
distribution = vw.groupby("fuelType")[["model"]].count().sort_values("model", ascending=False).reset_index()

plt.figure(figsize=(4,4)) # Set the figure size
plt.pie(
    distribution.model,
    labels=distribution.fuelType,
    autopct="%1.1f%%",
    startangle=140
)
plt.title('Distribution of Fuel Types')
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

# TASK 5
average_mileage = vw.groupby("model")[["mileage"]].mean().sort_values("model", ascending=True).reset_index()

plt.figure(figsize=(6, 6))
plt.bar(
    average_mileage["model"], 
    average_mileage["mileage"],
    color="maroon",
    width=0.4
    )
plt.xlabel("model")
plt.ylabel("average_mileage")
plt.title("My first chart")
plt.show()