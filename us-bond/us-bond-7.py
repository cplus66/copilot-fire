import pandas as pd
import matplotlib.pyplot as plt

# Hypothetical data for U.S. 10-year Treasury bonds from 2000 to 2025
data = {
    'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
             2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,
             2020, 2021, 2022, 2023, 2024, 2025],
    'Price': [103.81, 102.47, 100.34, 98.15, 97.27, 95.88, 94.57, 93.26,
              91.95, 90.64, 95.19, 96.50, 97.81, 99.12, 100.43, 105.44,
              107.22, 110.98, 112.77, 115.55, 137.22, 132.80, 122.57,
              110.48, 103.24, 97.27],
    'Yield': [6.03, 5.02, 4.61, 4.01, 4.27, 4.39, 4.78, 4.63, 3.66, 3.26,
              3.84, 3.36, 1.88, 2.35, 2.17, 2.27, 1.84, 2.41, 2.91, 1.92,
              0.93, 1.52, 2.75, 3.79, 4.36, 4.60],
    'Exchange Rate': [31.40, 33.80, 34.65, 34.60, 34.80, 33.88, 32.53, 32.77,
                      31.54, 33.01, 31.52, 29.47, 29.41, 30.03, 30.15, 32.50,
                      32.25, 29.65, 30.73, 30.40, 29.83, 27.88, 30.47, 30.52,
                      30.27, 32.75]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate additional column (Yield/Price)/Exchange Rate
df['(Yield/Price)/Exchange Rate'] = (df['Yield'] / df['Price']) / df['Exchange Rate']

# Display the DataFrame
print(df)

# Plotting Price, Yield, and (Yield/Price)/Exchange Rate over time
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot Price
ax1.set_xlabel('Year')
ax1.set_ylabel('Price', color='tab:blue')
ax1.plot(df['Year'], df['Price'], color='tab:blue', marker='o', label='Price')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Create a second y-axis to plot Yield and (Yield/Price)/Exchange Rate
ax2 = ax1.twinx()
ax2.set_ylabel('Yield & (Yield/Price)/Exchange Rate', color='tab:red')
ax2.plot(df['Year'], df['Yield'], color='tab:red', marker='x', label='Yield (%)')
ax2.plot(df['Year'], df['(Yield/Price)/Exchange Rate'], color='tab:green', marker='^', label='(Yield/Price)/Exchange Rate')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Add title and legends
fig.suptitle('Historical Prices, Yields, and (Yield/Price)/Exchange Rate of U.S. 10-year Treasury Bonds (2000-2025)')
fig.tight_layout()
fig.legend(loc='upper left')

# Display the plot
plt.grid(True)
plt.show()

