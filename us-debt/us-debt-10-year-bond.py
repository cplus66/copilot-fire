import matplotlib.pyplot as plt

# Data for U.S. government debt (in trillion USD)
us_debt = {
    1980: 0.91,
    1990: 3.23,
    2000: 5.67,
    2010: 13.56,
    2020: 26.95,
    2021: 28.43,
    2022: 31.42,
    2023: 34,
    2024: 35
}

# Data for U.S. 10-year bond yield rate (in percentage)
us_bond_yield = {
    1980: 11.46,
    1990: 8.55,
    2000: 6.03,
    2010: 3.22,
    2020: 0.89,
    2021: 1.45,
    2022: 2.95,
    2023: 3.96,
    2024: 4.21
}

# Extract years and values for plotting
years_debt = list(us_debt.keys())
debt = list(us_debt.values())

years_bond_yield = list(us_bond_yield.keys())
bond_yield = list(us_bond_yield.values())

# Plotting the data
fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:red'
ax1.set_xlabel('Year')
ax1.set_ylabel('Debt (in trillion USD)', color=color)
ax1.plot(years_debt, debt, marker='o', color=color, label='U.S. Government Debt')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('10-Year Bond Yield Rate (%)', color=color)
ax2.plot(years_bond_yield, bond_yield, marker='o', color=color, label='10-Year Bond Yield Rate')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title('Historical U.S. Government Debt and 10-Year Bond Yield Rate')
plt.grid(True)
plt.show()


