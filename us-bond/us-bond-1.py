import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Fetch historical data for U.S. 10-year Treasury bonds
start_date = '2000-01-01'
end_date = '2025-01-01'
df = web.DataReader('^TNX', 'fred', start_date, end_date)

# Plotting Yield over time
fig, ax = plt.subplots()
ax.plot(df.index, df['VALUE'], color='tab:red')
ax.set_xlabel('Date')
ax.set_ylabel('Yield (%)', color='tab:red')
ax.tick_params(axis='y', labelcolor='tab:red')

# Display the plot
plt.title('Historical Yields of U.S. 10-year Treasury Bonds (2000-2025)')
plt.show()

