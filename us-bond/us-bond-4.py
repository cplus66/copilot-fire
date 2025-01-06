import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Fetch historical data for U.S. 10-year Treasury bond yields
start_date = '2000-01-01'
end_date = '2025-01-01'
yield_data = web.DataReader('DGS10', 'fred', start_date, end_date)

# Corrected hypothetical price data to match dates
price_data = {
    'Date': pd.to_datetime(['2000-01-01', '2001-01-01', '2002-01-01', '2003-01-01', '2004-01-01',
                            '2005-01-01', '2006-01-01', '2007-01-01', '2008-01-01', '2009-01-01',
                            '2010-01-01', '2011-01-01', '2012-01-01', '2013-01-01', '2014-01-01',
                            '2015-01-01', '2016-01-01', '2017-01-01', '2018-01-01', '2019-01-01',
                            '2020-01-01', '2021-01-01', '2022-01-01', '2023-01-01', '2024-01-01', 
                            '2025-01-01']),
    'Price': [103.81, 102.47, 100.34, 98.15, 97.27, 95.88, 94.57, 93.26, 91.95, 90.64,
              95.19, 96.50, 97.81, 99.12, 100.43, 105.44, 107.22, 110.98, 112.77, 115.55,
              137.22, 132.80, 122.57, 110.48, 103.24, 97.27]
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

