# dashboard.py
# REST API Data Fetcher + Chart Output 📊

import matplotlib.pyplot as plt
from api_handler import fetch_data

#  API URL (your weather data)
url = "https://api.open-meteo.com/v1/forecast?latitude=11.01&longitude=76.96&hourly=temperature_2m"

data = fetch_data(url)

if data:

    # ⏰ Extract data
    times = data["hourly"]["time"][:24]  # first 24 hours
    temps = data["hourly"]["temperature_2m"][:24]

    # 🧠 Clean time for graph (only hour part)
    hours = [t.split("T")[1] for t in times]

    # 📊 Plot chart
    plt.figure(figsize=(10,5))
    plt.plot(hours, temps, marker='o')

    plt.title("Hourly Temperature Dashboard")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)

    plt.grid(True)
    plt.tight_layout()

    # 🚀 Show chart
    plt.show()

else:
    print(" Failed to fetch API data")