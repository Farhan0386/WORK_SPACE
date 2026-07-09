import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("gps_data.csv")
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df = df.sort_values(["VehicleID", "Timestamp"])

# Shifted coordinates for haversine
df["lat_prev"] = df.groupby("VehicleID")["Latitude"].shift()
df["lon_prev"] = df.groupby("VehicleID")["Longitude"].shift()

# Haversine distance
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # km
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)**2
    return 2 * R * np.arcsin(np.sqrt(a))

df["distance_km"] = haversine(df["Latitude"], df["Longitude"], df["lat_prev"], df["lon_prev"])

# Speed bins
bins = [0, 5, 20, np.inf]
labels = ["Gridlock", "Slow", "Free Flow"]
df["traffic_state"] = pd.cut(df["Speed"], bins=bins, labels=labels)

# Acceleration trends
df["speed_diff"] = df.groupby("VehicleID")["Speed"].diff()

# Scatter plot congestion
plt.figure(figsize=(10,6))
plt.scatter(df["Longitude"], df["Latitude"], c=df["Speed"], cmap="coolwarm", alpha=0.5)
plt.colorbar(label="Speed (km/h)")
plt.title("Congestion Map")
plt.show()

# Radar chart (weekly speeds)
weekly = df.groupby(df["Timestamp"].dt.day_name())["Speed"].mean()
angles = np.linspace(0, 2*np.pi, len(weekly), endpoint=False).tolist()
speeds = weekly.values.tolist()
speeds += speeds[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
ax.plot(angles, speeds, "o-", linewidth=2)
ax.fill(angles, speeds, alpha=0.25)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(weekly.index)
plt.title("Traffic Speeds by Day of Week")
plt.show()
