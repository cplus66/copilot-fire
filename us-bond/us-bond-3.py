import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Fetch historical data for U.S. 10-year Treasury bond yields
start_date = '2000-01-01'
end_date = '2025-01-01'
yield_data = web.DataReader('DGS10', 'fred', start_date, end_date)

# Hypothetical price data (since real bond prices are harder to find)
price_data = {
    'Date': pd.date_range(start=start_date, end=end_date, freq='A'),
    'Price': [103.81, 95.88, 95.19, 105.44, 137.22, 97.27, 100.34, 102.47, 98.15, 94.57, 100.21, 105.65, 110.98, 112.77, 107.14, 101.45, 99.01, 95.32, 90.87, 85.76, 80.66, 76.45, 81.57, 85.93, 89.34, 92.47]
}
price_df = pd.DataFrame(price_data)

# Create a plot
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot Yield
ax1.set_xlabel('Date')
ax1.set_ylabel('Yield (%)', color='tab:red')
ax1.plot(yield_data.index, yield_data['DGS10'], color='tab:red', label='Yield (%)')
ax1.tick_params(axis='y', labelcolor='tab:red')

# Create a second y-axis to plot Price
ax2 = ax1.twinx()
ax2.set_ylabel('Price', color='tab:blue')
ax2.plot(price_df['Date'], price_df['Price'], color='tab:blue', label='Price')
ax2.tick_params(axis='y', labelcolor='tab:blue')

# Add title and legend
fig.suptitle('Historical Prices and Yields of U.S. 10-year Treasury Bonds (2000-2025)')
fig.tight_layout()
fig.legend(loc='upper left')

# Display the plot
plt.show()

