import pandas as pd


def temperature_model(pressure, precipitation, wind_speed, time):
    return pressure * time**2 + precipitation * time + wind_speed


df = pd.read_csv("1_weather_modelling\weather_data.csv")
time = float(input("Enter time (in hours): "))

for index, row in df.iterrows():
    pressure = row["pressure"]
    precipitation = row["precipitation"]
    wind_speed = row["wind_speed"]

    predicted_temperature = temperature_model(pressure, precipitation, wind_speed, time)
    print(f"At time {time} hrs the temperature is: {predicted_temperature:.2f} °C")
