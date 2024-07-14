import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def temperature_model(pressure, precipitation, wind_speed, time):
    return pressure * time**2 + precipitation * time + wind_speed


# Read weather data from CSV file
df = pd.read_csv("1_weather_modelling\weather_data.csv")
time_values = np.linspace(0, 10, 100)  # Time range from 0 to 10 hours

# Plotting results for multiple sets of inputs
plt.figure(figsize=(10, 6))

for index, row in df.iterrows():
    pressure = row["pressure"]
    precipitation = row["precipitation"]
    wind_speed = row["wind_speed"]

    temperatures = temperature_model(pressure, precipitation, wind_speed, time_values)
    plt.plot(time_values, temperatures, label=f"Set {index + 1}")

plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Prediction")
plt.legend()
plt.show()
