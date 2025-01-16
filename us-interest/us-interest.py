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

# Retrieve the historical U.S. interest rate data (e.g., Effective Federal Funds Rate)
data = fred.get_series('FEDFUNDS')

# Convert to DataFrame for better visualization
df = pd.DataFrame(data, columns=['FEDFUNDS'])
df.index.name = 'Date'

# Resample the data to quarterly frequency, taking the last value of each period
df_quarterly = df.resample('QE').last()

# Display the first few rows of the DataFrame
print(df_quarterly.head())

# Plot the interest rate data
plt.figure(figsize=(10, 5))
plt.plot(df_quarterly.index, df_quarterly['FEDFUNDS'], label='Effective Federal Funds Rate')
plt.title('Historical Quarterly U.S. Interest Rates (Effective Federal Funds Rate)')
plt.xlabel('Date')
plt.ylabel('Interest Rate (%)')
plt.legend()
plt.grid(True)
plt.show()
