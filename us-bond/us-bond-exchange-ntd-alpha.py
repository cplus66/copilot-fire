import pandas as pd
from alpha_vantage.foreignexchange import ForeignExchange
import matplotlib.pyplot as plt

def read_api_key(file_path):
    """
    Reads the API key from a specified file.
    """
    with open(file_path, 'r') as file:
        api_key = file.read().strip()
    return api_key

# Path to the file containing the API key
file_path = '/home/cplus/.ssh/alpha-vantage.txt'

# Read the API key from the file
api_key = read_api_key(file_path)

# Initialize the Alpha Vantage ForeignExchange client with the API key
fx = ForeignExchange(key=api_key)

# Retrieve the USD to EUR exchange rate data
data_usd_eur, _ = fx.get_currency_exchange_monthly(from_symbol='USD', to_symbol='EUR')

# Retrieve the USD to NTD exchange rate data
data_usd_ntd, _ = fx.get_currency_exchange_monthly(from_symbol='USD', to_symbol='TWD')

# Convert to DataFrame for better visualization
df_usd_eur = pd.DataFrame.from_dict(data_usd_eur, orient='index').astype(float)
df_usd_ntd = pd.DataFrame.from_dict(data_usd_ntd, orient='index').astype(float)

# Convert index to datetime
df_usd_eur.index = pd.to_datetime(df_usd_eur.index)
df_usd_ntd.index = pd.to_datetime(df_usd_ntd.index)

# Resample the data to quarterly frequency, taking the last value of each period
df_usd_eur_quarterly = df_usd_eur.resample('Q').last()
df_usd_ntd_quarterly = df_usd_ntd.resample('Q').last()

# Display the first few rows of the DataFrames
print("USD to EUR Quarterly Data:\n", df_usd_eur_quarterly.head())
print("\nUSD to NTD Quarterly Data:\n", df_usd_ntd_quarterly.head())

# Plot the exchange rate data
plt.figure(figsize=(10, 5))
plt.plot(df_usd_eur_quarterly.index, df_usd_eur_quarterly['4. close'], label='USD/EUR')
plt.plot(df_usd_ntd_quarterly.index, df_usd_ntd_quarterly['4. close'], label='USD/NTD')
plt.title('Historical Quarterly USD to EUR and USD to NTD Exchange Rates')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.grid(True)
plt.show()
