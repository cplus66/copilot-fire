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
data, _ = fx.get_currency_exchange_monthly(from_symbol='USD', to_symbol='EUR')

# Convert to DataFrame for better visualization
df = pd.DataFrame.from_dict(data, orient='index').astype(float)

# Convert index to datetime
df.index = pd.to_datetime(df.index)

# Resample the data to quarterly frequency, taking the last value of each period
df_quarterly = df.resample('QE').last()

# Display the first few rows of the DataFrame
print(df_quarterly.head())

# Plot the exchange rate data
plt.figure(figsize=(10, 5))
plt.plot(df_quarterly.index, df_quarterly['4. close'], label='USD/EUR')
plt.title('Historical Quarterly USD to EUR Exchange Rate')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.grid(True)
plt.show()
