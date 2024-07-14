def temperature(pressure, precipiation, wind_speed, time):
    return pressure * time**2 + precipiation * time + wind_speed


pressure = 1.0
precipiation = -3.0
wind_speed = 2.0
time = 5

print(
    "At time",
    time,
    "hrs the temperature is :",
    temperature(pressure, precipiation, wind_speed, time),
    "°C",
)
