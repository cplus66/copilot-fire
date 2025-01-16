import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred

def read_api_key(file_path):
    """
    Reads the API key from a specified file.
    """
    with open(file_path, 'r') as file:
        api_key = file.read().strip()
    return api_key

# Path to the file containing the API key
file_path = '/home/cplus/.ssh/fred-api.txt'

# Read the API key from the file
api_key = read_api_key(file_path)

# Initialize the Fred client with the API key
fred = Fred(api_key=api_key)

# Retrieve the historical U.S. 10-year bond yield rate data
bond_yield_data = fred.get_series('DGS10')

# Retrieve the historical U.S. federal funds interest rate data
interest_rate_data = fred.get_series('FEDFUNDS')

# Convert to DataFrames for better visualization
df_bond_yield = pd.DataFrame(bond_yield_data, columns=['10-Year Treasury Yield'])
df_interest_rate = pd.DataFrame(interest_rate_data, columns=['Federal Funds Rate'])

# Convert index to datetime
df_bond_yield.index = pd.to_datetime(df_bond_yield.index)
df_interest_rate.index = pd.to_datetime(df_interest_rate.index)

# Display the first few rows of the DataFrames
print("U.S. 10-Year Bond Yield Rate Data:\n", df_bond_yield.head())
print("\nU.S. Federal Funds Interest Rate Data:\n", df_interest_rate.head())

# Plot the bond yield rate and interest rate data
fig, ax1 = plt.subplots(figsize=(12, 6))

color = 'tab:blue'
ax1.set_xlabel('Date')
ax1.set_ylabel('10-Year Treasury Yield (%)', color=color)
ax1.plot(df_bond_yield.index, df_bond_yield['10-Year Treasury Yield'], color=color, label='10-Year Treasury Yield')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:green'
ax2.set_ylabel('Federal Funds Rate (%)', color=color)  # we already handled the x-label with ax1
ax2.plot(df_interest_rate.index, df_interest_rate['Federal Funds Rate'], color=color, label='Federal Funds Rate')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title('Historical U.S. 10-Year Bond Yield Rate and Federal Funds Interest Rate')
plt.show()
