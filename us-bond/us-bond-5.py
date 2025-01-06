import pandas as pd
import matplotlib.pyplot as plt

# Hypothetical price data for U.S. 10-year Treasury bonds from 2000 to 2025
price_data = {
    'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
             2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,
             2020, 2021, 2022, 2023, 2024, 2025],
    'Price': [103.81, 102.47, 100.34, 98.15, 97.27, 95.88, 94.57, 93.26,
              91.95, 90.64, 95.19, 96.50, 97.81, 99.12, 100.43, 105.44,
              107.22, 110.98, 112.77, 115.55, 137.22, 132.80, 122.57,
              110.48, 103.24, 97.27]
}

# Create DataFrame
price_df = pd.DataFrame(price_data)

# Plotting Price over time
plt.figure(figsize=(12, 6))
plt.plot(price_df['Year'], price_df['Price'], color='tab:blue', marker='o')
plt.xlabel('Year')
plt.ylabel('Price')
plt.title('Historical Prices of U.S. 10-year Treasury Bonds (2000-2025)')
plt.grid(True)

# Display the plot
plt.show()

