import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create sample data
rows = []
vehicles = ["TX-1", "TX-2", "TX-3"]
start_date = pd.Timestamp("2025-01-01")

for v in range(len(vehicles)):
    lat = 28.5 + v * 0.1
    lon = 77.1 + v * 0.1

    for d in range(15):
        lat += 0.01
        lon += 0.01
        speed = 10 + d * 4 + v * 12

        rows.append({
            "VehicleID": vehicles[v],
            "Timestamp": start_date + pd.Timedelta(days=d),
            "Latitude": round(lat, 3),
            "Longitude": round(lon, 3),
            "Speed": speed
        })

# Save dataset
df = pd.DataFrame(rows)
df.to_csv("taxi_gps_dataset.csv", index=False)

# Load dataset
df = pd.read_csv("taxi_gps_dataset.csv")

# Convert date
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Sort data
df = df.sort_values(["VehicleID", "Timestamp"])

# Previous location
df["PrevLat"] = df.groupby("VehicleID")["Latitude"].shift(1)
df["PrevLon"] = df.groupby("VehicleID")["Longitude"].shift(1)

df["PrevLat"] = df["PrevLat"].fillna(df["Latitude"])
df["PrevLon"] = df["PrevLon"].fillna(df["Longitude"])

# Simple distance
df["Distance"] = np.sqrt(
    (df["Latitude"] - df["PrevLat"])**2 +
    (df["Longitude"] - df["PrevLon"])**2
)

# Grid groups
df["Grid"] = (
    df["Latitude"].round(1).astype(str)
    + ", " +
    df["Longitude"].round(1).astype(str)
)

# Speed categories
bins = [20, 40, 60]
labels = ["Gridlock", "Slow", "Normal", "Free Flow"]

df["SpeedClass"] = [labels[i] for i in np.digitize(df["Speed"], bins)]

# Speed difference
df["SpeedDiff"] = 0

for vehicle in vehicles:
    i = df[df["VehicleID"] == vehicle].index
    s = df.loc[i, "Speed"]
    df.loc[i, "SpeedDiff"] = np.diff(s, prepend=s.iloc[0])

# Output
print(df.head(10))
print("\nSpeed Categories")
print(df["SpeedClass"].value_counts())
print("\nAverage Speed:", df["Speed"].mean())

# Scatter plot
plt.scatter(df["Longitude"], df["Latitude"], c=df["Speed"])
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Taxi GPS Points")
plt.colorbar(label="Speed")
plt.show()

# Bar chart
avg = df.groupby("VehicleID")["Speed"].mean()

plt.bar(avg.index, avg.values)
plt.xlabel("Vehicle")
plt.ylabel("Average Speed")
plt.title("Average Speed by Vehicle")
plt.show()