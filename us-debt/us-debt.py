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

# Extract years and debt values for plotting
years = list(us_debt.keys())
debt = list(us_debt.values())

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(years, debt, marker='o', label='U.S. Government Debt')

# Adding titles and labels
plt.title('Historical U.S. Government Debt')
plt.xlabel('Year')
plt.ylabel('Debt (in trillion USD)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
