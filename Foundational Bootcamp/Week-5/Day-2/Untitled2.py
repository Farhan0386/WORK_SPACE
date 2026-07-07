import pandas as pd
import numpy as np

# Generate 100 students
roll = np.arange(1, 101)
names = [f"Student_{i}" for i in roll]

# Random marks between 0–100
python = np.random.randint(0, 101, 100)
java = np.random.randint(0, 101, 100)
ml = np.random.randint(0, 101, 100)
cloud = np.random.randint(0, 101, 100)

# Random attendance between 50–100%
attendance = np.random.randint(50, 101, 100)

df = pd.DataFrame({
    'Roll': roll,
    'Name': names,
    'Python': python,
    'Java': java,
    'ML': ml,
    'Cloud': cloud,
    'Attendance': attendance
})

df['Total'] = df[['Python','Java','ML','Cloud']].sum(axis=1)
df['Percentage'] = df['Total'] / 4

def grade(p):
    if p >= 85: return 'A'
    elif p >= 70: return 'B'
    elif p >= 50: return 'C'
    else: return 'D'

df['Grade'] = df['Percentage'].apply(grade)
df['Rank'] = df['Total'].rank(method='dense', ascending=False).astype(int)

top10 = df.nsmallest(10, 'Rank')
print(top10)

mask = ((df[['Python','Java','ML','Cloud']] < 40).sum(axis=1) >= 2)
low_perf = df[mask]
print(low_perf)

dept_topper = {}
for subject in ['Python','Java','ML','Cloud']:
    topper = df.loc[df[subject].idxmax()]
    dept_topper[subject] = topper[['Roll','Name',subject]]
print(dept_topper)

low_attendance = df[df['Attendance'] < 75]
print(low_attendance)

top10.to_csv('topper_list.csv', index=False)
print("Topper list exported successfully!")
