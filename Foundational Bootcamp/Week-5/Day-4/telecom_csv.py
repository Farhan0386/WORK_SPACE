import pandas as pd
import numpy as np

# Parameters
n_vehicles = 50
n_points_per_vehicle = 200  # total rows = 50 * 200 = 10,000
np.random.seed(42)

rows = []
for vid in range(1, n_vehicles+1):
    # Random start location (Delhi approx lat/lon)
    lat, lon = 28.6 + np.random.randn()/100, 77.2 + np.random.randn()/100
    speed = np.random.randint(0, 60)  # km/h
    
    for t in range(n_points_per_vehicle):
        timestamp = pd.Timestamp("2026-07-01") + pd.Timedelta(minutes=5*t)
        
        # Simulate movement
        lat += np.random.randn()/1000
        lon += np.random.randn()/1000
        speed = max(0, speed + np.random.randint(-5, 6))  # fluctuate
        
        rows.append([vid, timestamp, lat, lon, speed])

# Build DataFrame
df = pd.DataFrame(rows, columns=["VehicleID", "Timestamp", "Latitude", "Longitude", "Speed"])

# Save to CSV
df.to_csv("gps_data.csv", index=False)

print("gps_data.csv created with", len(df), "rows")
