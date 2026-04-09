import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Create Data (1900 to 2024)
years = np.array(range(1900, 2025)).reshape(-1, 1)
# Simulating temp increase with some random "weather" noise
temp_anomaly = 0.015 * (years - 1900) + np.random.normal(0, 0.15, size=years.shape)

# Train AI Model
model = LinearRegression()
model.fit(years, temp_anomaly)

# Predict Future (to 2075)
future_years = np.array(range(2025, 2076)).reshape(-1, 1)
future_preds = model.predict(future_years)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# GRAPH 1: The Trend Line (Time vs Temp)
ax1.scatter(years, temp_anomaly, color='royalblue', s=10, label='Historical Data')
ax1.plot(years, model.predict(years), color='red', label='AI Trend Line')
ax1.plot(future_years, future_preds, color='red', linestyle='--', label='AI Future Prediction')
ax1.set_title('Graph 1: Temperature Trend Over Time')
ax1.set_xlabel('Year')
ax1.set_ylabel('Temp Anomaly (°C)')
ax1.legend()
ax1.grid(True, alpha=0.3)

# The Distribution Shift (Frequency of Heat)
early_years = temp_anomaly[:30]
recent_years = temp_anomaly[-30:]

sns.kdeplot(early_years.flatten(), ax=ax2, fill=True, color="blue", label="Early 1900s")
sns.kdeplot(recent_years.flatten(), ax=ax2, fill=True, color="red", label="Recent Years")
ax2.set_title('Graph 2: Distribution Shift (Climate Variance)')
ax2.set_xlabel('Temperature Anomaly (°C)')
ax2.set_ylabel('Frequency of Occurrence')
ax2.legend()

plt.tight_layout()
plt.show()

