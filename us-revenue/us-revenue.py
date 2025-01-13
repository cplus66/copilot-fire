import matplotlib.pyplot as plt

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

# Extract years and revenue values for plotting
years = list(us_revenue.keys())
revenue = list(us_revenue.values())

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(years, revenue, marker='o', label='U.S. Government Revenue')

# Adding titles and labels
plt.title('Historical U.S. Government Revenue')
plt.xlabel('Year')
plt.ylabel('Revenue (in trillion USD)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
