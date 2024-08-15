import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
import seaborn as sns

# Simulate data for 7 days
num_days = 7
dates = [datetime.now() - timedelta(days=i) for i in range(num_days)]
dates.reverse()

# Generates random data
np.random.seed(42)
heart_rate = np.random.randint(60, 100, size=num_days)  # Simulating heart rate in bpm
steps = np.random.randint(4000, 12000, size=num_days)   # Simulating steps taken
body_temp = np.random.normal(98.6, 0.5, size=num_days)  # Simulating body temperature in Fahrenheit

# Creates a DataFrame
data = pd.DataFrame({
    'Date': dates,
    'Heart Rate (bpm)': heart_rate,
    'Steps Taken': steps,
    'Body Temperature (F)': body_temp
})

print(data)

# Analyze the Data

# Analyze heart rate data
average_heart_rate = data['Heart Rate (bpm)'].mean()
print(f"Average Heart Rate: {average_heart_rate:.2f} bpm")

# Check for anomalies in heart rate (e.g., too high or too low)
anomalies = data[(data['Heart Rate (bpm)'] > 90) | (data['Heart Rate (bpm)'] < 65)]
print("Heart Rate Anomalies Detected:")
print(anomalies)

# Analyze steps taken
average_steps = data['Steps Taken'].mean()
print(f"Average Steps Taken: {average_steps:.0f}")

# Analyze body temperature
average_temp = data['Body Temperature (F)'].mean()
print(f"Average Body Temperature: {average_temp:.2f} F")

plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Heart Rate (bpm)'], marker='o', linestyle='-', color='r', label='Heart Rate (bpm)')
plt.axhline(average_heart_rate, color='r', linestyle='--', label=f'Avg Heart Rate ({average_heart_rate:.2f} bpm)')
plt.plot(data['Date'], data['Body Temperature (F)'], marker='o', linestyle='-', color='g', label='Body Temperature (F)')
plt.axhline(average_temp, color='g', linestyle='--', label=f'Avg Temp ({average_temp:.2f} F)')
plt.title('Heart Rate & Body Temperature Over the Last Week')
plt.xlabel('Date')
plt.ylabel('Measurement')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
sns.regplot(x=data['Steps Taken'], y=data['Heart Rate (bpm)'], color='blue', line_kws={"color":"red"})
plt.title('Heart Rate vs Steps Taken')
plt.xlabel('Steps Taken')
plt.ylabel('Heart Rate (bpm)')
plt.grid(True)
plt.show()


plt.figure(figsize=(10, 6))
sns.regplot(x=data['Body Temperature (F)'], y=data['Heart Rate (bpm)'], color='green', line_kws={"color":"red"})
plt.title('Heart Rate vs Body Temperature')
plt.xlabel('Body Temperature (F)')
plt.ylabel('Heart Rate (bpm)')
plt.grid(True)
plt.show()


# Reshape data for linear regression
X = data[['Steps Taken', 'Body Temperature (F)']]
y = data['Heart Rate (bpm)']

# Fit the model
model = LinearRegression()
model.fit(X, y)

# Predict heart rate
data['Predicted Heart Rate'] = model.predict(X)

# Compare actual vs predicted heart rate
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Heart Rate (bpm)'], marker='o', linestyle='-', color='r', label='Actual Heart Rate')
plt.plot(data['Date'], data['Predicted Heart Rate'], marker='x', linestyle='--', color='b', label='Predicted Heart Rate')
plt.title('Actual vs Predicted Heart Rate')
plt.xlabel('Date')
plt.ylabel('Heart Rate (bpm)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()
