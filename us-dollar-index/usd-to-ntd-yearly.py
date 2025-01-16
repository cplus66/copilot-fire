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

# Retrieve the USD to NTD exchange rate data
data, _ = fx.get_currency_exchange_monthly(from_symbol='USD', to_symbol='TWD')

# Convert to DataFrame for better visualization
df = pd.DataFrame.from_dict(data, orient='index').astype(float)

# Convert index to datetime
df.index = pd.to_datetime(df.index)

# Resample the data to yearly frequency using 'YE' (year-end), taking the last value of each year
df_yearly = df.resample('YE').last()

# Display the first few rows of the DataFrame
print(df_yearly.head())

# Plot the exchange rate data
plt.figure(figsize=(10, 5))
plt.plot(df_yearly.index, df_yearly['4. close'], label='USD/NTD')
plt.title('Historical Yearly USD to NTD Exchange Rate')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.grid(True)
plt.show()
