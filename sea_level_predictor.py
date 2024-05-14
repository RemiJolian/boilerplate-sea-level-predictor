
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the data from the CSV file
data = pd.read_csv('epa-sea-level.csv')

# Create a scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='Actual Data')

# Calculate the line of best fit for all the data
slope, intercept, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
plt.plot(data['Year'], slope*data['Year'] + intercept, color='red', label='Line of Best Fit (All Data)')

# Calculate the line of best fit for data from year 2000 onwards
recent_data = data[data['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
plt.plot(data['Year'], slope_recent*data['Year'] + intercept_recent, color='green', label='Line of Best Fit (Since 2000)')

# Extend the lines to predict sea level rise in 2050
plt.plot([1883, 2050], [slope*1883 + intercept, slope*2050 + intercept], linestyle='--', color='red', label='Prediction to 2050 (All Data)')
plt.plot([2000, 2050], [slope_recent*2000 + intercept_recent, slope_recent*2050 + intercept_recent], linestyle='--', color='green', label='Prediction to 2050 (Since 2000)')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

plt.legend()
plt.grid(True)
plt.show()