# import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

# # Sample DataFrame
# data = {
# 'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
# 'Sales': [2500, 2700, 3000, 3200]

# }

# df = pd.DataFrame(data)

# # Plot using matplotlib
# plt.plot(df['Month' ], df['Sales'], marker='o')
# plt.title('Monthly Sales')
# plt.xlabel('Month')
# plt.ylabel('Sales')
# plt.grid(True)
# plt.show()
# import pandas as pd
# import matplotlib.pyplot as plt

# # ==========================
# # Sample Data
# # ==========================
# data = {
#     'Region': ['North', 'South', 'East', 'West'],
#     'Sales': [10000, 15000, 12000, 13000]
# }

# # Create DataFrame
# df = pd.DataFrame(data)

# # ==========================
# # Plot Bar Chart
# # ==========================
# plt.bar(df['Region'], df['Sales'], color='skyblue')

# plt.title('Sales by Region')
# plt.xlabel('Region')
# plt.ylabel('Sales')

# plt.grid(axis='y')

# plt.show()

# Import libraries

# from matplotlib import pyplot as plt

# import numpy as np
# # Creating dataset
# cars = ['AUDI', 'BMW', 'FORD',
# 'TESLA', 'JAGUAR', 'MERCEDES']

# data = [23, 17, 35, 29, 12, 41]
# # Creating plot
# fig = plt.figure(figsize=(10, 7))

# plt.pie(data, labels=cars)
# # show plot
# plt.show()

# import matplotlib.pyplot as plt

# # ==========================
# # Sample Data
# # ==========================
# ages = [
#     2, 5, 70, 40, 30, 45, 50, 45, 43, 40,
#     44, 60, 7, 13, 57, 18, 90, 77, 32, 21,
#     20, 40
# ]

# # ==========================
# # Histogram Settings
# # ==========================
# data_range = (0, 100)   # Avoid using the name 'range'
# bins = 10               # Number of intervals

# # ==========================
# # Plot Histogram
# # ==========================
# plt.hist(
#     ages,
#     bins=bins,
#     range=data_range,
#     color="green",
#     histtype="bar",
#     rwidth=0.8
# )

# # ==========================
# # Labels & Title
# # ==========================
# plt.title("My Histogram")
# plt.xlabel("Age")
# plt.ylabel("Number of People")

# # Show horizontal grid lines
# plt.grid(axis="y")

# # Display the graph
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# # ==========================
# # Create 3 × 3 Subplots
# # ==========================
# fig, ax = plt.subplots(3, 3)

# # ==========================
# # Draw Random Line Graphs
# # ==========================
# for i in ax:
#     for j in i:
#         j.plot(np.random.randint(0, 5, 5))

# # ==========================
# # Display Graphs
# # ==========================
# plt.show()



import matplotlib.pyplot as plt

# ==========================
# Sample Data
# ==========================
x_axis_value = [6, 7, 9, 8, 2, 16, 3, 6, 4, 14, 13, 4, 1]

y_axis_value = [98, 87, 84, 86, 99, 85, 102, 89, 96, 78, 77, 83, 81]

# ==========================
# Create Scatter Plot
# ==========================
plt.scatter(
    x_axis_value,
    y_axis_value,
    color="blue",
    marker="o"
)

# ==========================
# Labels & Title
# ==========================
plt.title("Scatter Plot")
plt.xlabel("X-axis Values")
plt.ylabel("Y-axis Values")

# Show grid
plt.grid(True)

# Display the plot
plt.show()