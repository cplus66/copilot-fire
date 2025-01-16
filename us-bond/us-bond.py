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
data = fred.get_series('DGS10')

# Convert to DataFrame for better visualization
df = pd.DataFrame(data, columns=['10-Year Treasury Constant Maturity Rate'])
df.index.name = 'Date'

# Display the first few rows of the DataFrame
print(df.head())

# Plot the bond yield rate data
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['10-Year Treasury Constant Maturity Rate'], label='10-Year Treasury Rate')
plt.title('Historical U.S. 10-Year Bond Yield Rate')
plt.xlabel('Date')
plt.ylabel('Yield Rate (%)')
plt.legend()
plt.grid(True)
plt.show()
