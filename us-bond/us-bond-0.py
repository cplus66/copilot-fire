import pandas as pd
import matplotlib.pyplot as plt

# Sample data of historical prices and yields
data = {
    'Year': [2000, 2005, 2010, 2015, 2020, 2025],
    'Price': [103.81, 95.88, 95.19, 105.44, 137.22, 97.27],
    'Yield': [6.03, 4.39, 3.84, 2.27, 0.93, 4.60]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plotting Price and Yield over time
fig, ax1 = plt.subplots()

# Plot Price
ax1.set_xlabel('Year')
ax1.set_ylabel('Price', color='tab:blue')
ax1.plot(df['Year'], df['Price'], color='tab:blue', marker='o')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Create a second y-axis to plot Yield
ax2 = ax1.twinx()
ax2.set_ylabel('Yield (%)', color='tab:red')
ax2.plot(df['Year'], df['Yield'], color='tab:red', marker='x')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Add title and legends
fig.suptitle('Historical Prices and Yields of U.S. 10-year Treasury Bonds (2000-2025)')
ax1.legend(['Price'], loc='upper left')
ax2.legend(['Yield'], loc='upper right')

# Display the plot
plt.show()

