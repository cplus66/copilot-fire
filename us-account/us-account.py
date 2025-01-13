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

# Data for U.S. government revenue (in trillion USD)
us_revenue = {
    1980: 0.5171,
    1990: 1.03,
    2000: 2.03,
    2010: 2.16,
    2020: 3.42,
    2021: 4.05,
    2022: 4.90,
    2023: 4.44,
    2024: 4.92
}

# Extract years and values for plotting
years_debt = list(us_debt.keys())
debt = list(us_debt.values())

years_revenue = list(us_revenue.keys())
revenue = list(us_revenue.values())

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(years_debt, debt, marker='o', label='U.S. Government Debt')
plt.plot(years_revenue, revenue, marker='o', label='U.S. Government Revenue')

# Adding titles and labels
plt.title('Historical U.S. Government Debt and Revenue')
plt.xlabel('Year')
plt.ylabel('Amount (in trillion USD)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
