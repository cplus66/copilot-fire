import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Fetch historical data for U.S. 10-year Treasury bond yields
start_date = '2000-01-01'
end_date = '2025-01-01'
yield_data = web.DataReader('DGS10', 'fred', start_date, end_date)

# Plotting Yield over time
plt.figure(figsize=(12, 6))
plt.plot(yield_data.index, yield_data['DGS10'], color='tab:red', marker='o')
plt.xlabel('Date')
plt.ylabel('Yield (%)')
plt.title('Historical Yields of U.S. 10-year Treasury Bonds (2000-2025)')
plt.grid(True)

# Display the plot
plt.show()

