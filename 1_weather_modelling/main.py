def temperature(pressure, precipiation, wind_speed, time):
    return pressure * time**2 + precipiation * time + wind_speed


pressure = float(input("Enter atmospheric pressure (in hPa): "))
precipitation = float(input("Enter precipitation (in mm): "))
wind_speed = float(input("Enter wind speed (in m/s): "))
time = float(input("Enter time (in hours): "))

print(
    "At time",
    time,
    "hrs the temperature is :",
    temperature(pressure, precipiation, wind_speed, time),
    "°C",
)
