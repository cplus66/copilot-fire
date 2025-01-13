import matplotlib.pyplot as plt
import datetime

# Historical data for U.S. 10-year bond yield rate (in percentage)
dates = [datetime.date(year, 1, 1) for year in range(2015, 2026)]
bond_yields = [2.14, 1.84, 2.33, 2.91, 2.14, 0.89, 1.45, 2.95, 3.96, 4.21, 4.62]

# Historical data for USD to NTD exchange rate
exchange_rates = [31.50, 32.00, 30.50, 29.50, 28.50, 27.50, 26.50, 27.00, 28.00, 29.00, 33.11]

fig, ax1 = plt.subplots()

# Plotting U.S. 10-year bond yield rate
ax1.set_xlabel('Year')
ax1.set_ylabel('U.S. 10-year Bond Yield (%)', color='tab:red')
ax1.plot(dates, bond_yields, color='tab:red', label='U.S. 10-year Bond Yield')
ax1.tick_params(axis='y', labelcolor='tab:red')

# Creating a second y-axis for the exchange rate
ax2 = ax1.twinx()
ax2.set_ylabel('USD to NTD Exchange Rate', color='tab:green')
ax2.plot(dates, exchange_rates, color='tab:green', label='USD to NTD Exchange Rate')
ax2.tick_params(axis='y', labelcolor='tab:green')

# Adding title and legend
plt.title('U.S. 10-year Bond Yield Rate and USD to NTD Exchange Rate (2015-2025)')
fig.tight_layout()
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

plt.show()
