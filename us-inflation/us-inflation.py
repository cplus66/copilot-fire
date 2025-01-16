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

# Calculate the monthly inflation rate
monthly_inflation_rate = cpi_data.pct_change() * 100

# Convert to DataFrame for better visualization
inflation_df = pd.DataFrame({
    'CPIAUCSL': cpi_data,
    'Monthly Inflation Rate (%)': monthly_inflation_rate
})

# Display the first few rows of the DataFrame
print(inflation_df.head())

# Plot the inflation rate
plt.figure(figsize=(10, 5))
plt.plot(inflation_df.index, inflation_df['Monthly Inflation Rate (%)'], label='Monthly Inflation Rate (%)')
plt.title('Monthly U.S. Inflation Rate')
plt.xlabel('Date')
plt.ylabel('Inflation Rate (%)')
plt.legend()
plt.grid(True)
plt.show()
