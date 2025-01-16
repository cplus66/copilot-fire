import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred
from alpha_vantage.foreignexchange import ForeignExchange

def read_api_key(file_path):
    """
    Reads the API key from a specified file.
    """
    with open(file_path, 'r') as file:
        api_key = file.read().strip()
    return api_key

# Paths to the files containing the API keys
fred_api_path = '/home/cplus/.ssh/fred-api.txt'
alpha_vantage_api_path = '/home/cplus/.ssh/alpha-vantage.txt'

# Read the API keys from the files
fred_api_key = read_api_key(fred_api_path)
alpha_vantage_api_key = read_api_key(alpha_vantage_api_path)

# Initialize the Fred client with the API key
fred = Fred(api_key=fred_api_key)

# Retrieve the historical U.S. 10-year bond yield rate data
bond_yield_data = fred.get_series('DGS10')

# Initialize the Alpha Vantage ForeignExchange client with the API key
fx = ForeignExchange(key=alpha_vantage_api_key)

# Retrieve the USD to NTD exchange rate data
usd_ntd_data, _ = fx.get_currency_exchange_monthly(from_symbol='USD', to_symbol='TWD')

# Convert to DataFrames for better visualization
df_bond_yield = pd.DataFrame(bond_yield_data, columns=['10-Year Treasury Yield'])
df_usd_ntd = pd.DataFrame.from_dict(usd_ntd_data, orient='index').astype(float)

# Convert index to datetime
df_bond_yield.index = pd.to_datetime(df_bond_yield.index)
df_usd_ntd.index = pd.to_datetime(df_usd_ntd.index)

# Resample the data to quarterly frequency, taking the last value of each period
df_bond_yield_quarterly = df_bond_yield.resample('Q').last()
df_usd_ntd_quarterly = df_usd_ntd.resample('Q').last()

# Plot the bond yield rate and exchange rate data
fig, ax1 = plt.subplots(figsize=(12, 6))

color = 'tab:blue'
ax1.set_xlabel('Date')
ax1.set_ylabel('10-Year Treasury Yield (%)', color=color)
ax1.plot(df_bond_yield_quarterly.index, df_bond_yield_quarterly['10-Year Treasury Yield'], color=color, label='10-Year Treasury Yield')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:green'
ax2.set_ylabel('USD/NTD Exchange Rate', color=color)  # we already handled the x-label with ax1
ax2.plot(df_usd_ntd_quarterly.index, df_usd_ntd_quarterly['4. close'], color=color, label='USD/NTD Exchange Rate')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title('Historical Quarterly U.S. 10-Year Bond Yield Rate and USD to NTD Exchange Rate')
plt.show()
