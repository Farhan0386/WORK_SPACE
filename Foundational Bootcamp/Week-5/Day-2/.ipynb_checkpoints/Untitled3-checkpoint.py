import pandas as pd
import numpy as np

# -------------------------------
# Step 1: Generate Employee Dataset
# -------------------------------
emp_id = np.arange(1, 501)

departments = ['IT', 'HR', 'Finance', 'Marketing', 'Sales']
dept = np.random.choice(departments, 500)

experience = np.random.randint(1, 31, 500)       # 1–30 years
salary = np.random.randint(30000, 150001, 500)   # 30k–150k
performance = np.random.randint(1, 6, 500)       # Rating 1–5

df = pd.DataFrame({
    'EmpID': emp_id,
    'Department': dept,
    'Experience': experience,
    'Salary': salary,
    'Performance': performance
})

print("Sample Data:\n", df.head())

# -------------------------------
# Step 2: Save dataset as CSV & Excel
# -------------------------------
df.to_csv('employees.csv', index=False)
df.to_excel('employees.xlsx', index=False)

# -------------------------------
# Step 3: Read both files
# -------------------------------
df_csv = pd.read_csv('employees.csv')
df_excel = pd.read_excel('employees.xlsx')

# -------------------------------
# Step 4: Verify identical data
# -------------------------------
print("Files identical:", df_csv.equals(df_excel))

# -------------------------------
# Step 5: Average salary department-wise
# -------------------------------
avg_salary = df.groupby('Department')['Salary'].mean()
print("Average Salary by Department:\n", avg_salary)

# -------------------------------
# Step 6: Highest performer
# -------------------------------
highest_perf = df.loc[df['Performance'].idxmax()]
print("Highest Performer:\n", highest_perf)

# -------------------------------
# Step 7: Employees with salary > department average
# -------------------------------
dept_avg = df.groupby('Department')['Salary'].transform('mean')
above_avg = df[df['Salary'] > dept_avg]
print("Employees above department average salary:\n", above_avg.head())

# -------------------------------
# Step 8: Employees with >15 years experience but performance <3
# -------------------------------
low_perf_exp = df[(df['Experience'] > 15) & (df['Performance'] < 3)]
print("Low performance but experienced employees:\n", low_perf_exp.head())

# -------------------------------
# Step 9: Bonus column (Perf ≥4 → 10%, else 5%)
# -------------------------------
df['Bonus'] = np.where(df['Performance'] >= 4,
                       df['Salary'] * 0.10,
                       df['Salary'] * 0.05)

print("Data with Bonus:\n", df.head())

# -------------------------------
# Step 10: Export only employees with Bonus > ₹10,000
# -------------------------------
bonus_above_10k = df[df['Bonus'] > 10000]
bonus_above_10k.to_csv('bonus_above_10k.csv', index=False)
bonus_above_10k.to_excel('bonus_above_10k.xlsx', index=False)

print("Exported employees with bonus above ₹10,000 successfully!")
