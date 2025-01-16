from fredapi import Fred
import pandas as pd
import matplotlib.pyplot as plt

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

# Retrieve data for Consumer Price Index for All Urban Consumers: All Items (CPIAUCSL)
cpi_data = fred.get_series('CPIAUCSL')

# Convert to DataFrame for better visualization
cpi_df = pd.DataFrame({
    'CPIAUCSL': cpi_data
})

# Display the first few rows of the DataFrame
print(cpi_df.head())

# Plot the CPI data
plt.figure(figsize=(10, 5))
plt.plot(cpi_df.index, cpi_df['CPIAUCSL'], label='CPIAUCSL')
plt.title('Historical U.S. Consumer Price Index (CPI)')
plt.xlabel('Date')
plt.ylabel('CPI')
plt.legend()
plt.grid(True)
plt.show()
