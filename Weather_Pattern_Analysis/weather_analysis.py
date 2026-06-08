import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
data = pd.read_csv("weather_data.csv")

print("\nWeather Pattern Analysis")
print("-" * 30)

# Basic Statistics
avg_temp = data["Temperature"].mean()
max_temp = data["Temperature"].max()
min_temp = data["Temperature"].min()
total_rainfall = data["Rainfall"].sum()

print("Average Temperature:", round(avg_temp, 2), "°C")
print("Maximum Temperature:", max_temp, "°C")
print("Minimum Temperature:", min_temp, "°C")
print("Total Rainfall:", total_rainfall, "mm")

# Create 2 charts in one window
plt.figure(figsize=(12, 5))

# Temperature Trend
plt.subplot(1, 2, 1)
plt.plot(
    data["Date"],
    data["Temperature"],
    marker="o"
)
plt.title("Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)

# Rainfall Trend
plt.subplot(1, 2, 2)
plt.bar(
    data["Date"],
    data["Rainfall"]
)
plt.title("Rainfall Analysis")
plt.xlabel("Date")
plt.ylabel("Rainfall (mm)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()