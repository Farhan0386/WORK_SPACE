import pandas as pd


data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

df = pd.DataFrame(data)

# Selecting a column
print(df['Name'])

# Adding a new column
df['Salary'] = [70000, 80000, 120000, 90000]
# Save to CSV without index
df.to_csv('output.csv', index=False)

print("CSV file created successfully!")
print(df)

# Display basic statistics
print(df.describe())

# Filtering data (Age > 30)
df_filtered = df[df['Age'] > 30]
print(df_filtered[["Age"]])

# Sorting data by Age
df_sorted = df.sort_values(by='Age')
print(df_sorted)

#  Selecting  rows  by  label
print( df. loc [1])

#  Selecting  rows  by  position 
print(df.iloc[2])

#  Slicing  Data Frames 
print( df. iloc [1:3])
