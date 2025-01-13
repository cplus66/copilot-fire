import matplotlib.pyplot as plt

# Data for government revenue (in trillion USD)
revenue_data = {
    'United States': {
        2020: 3.42,
        2021: 4.05,
        2022: 4.90,
        2023: 4.44,
        2024: 4.92
    },
    'China': {
        2022: 3.1,
        2023: 3.2,
        2024: 3.4
    },
    'Japan': {
        2022: 1.7,
        2023: 1.8,
        2024: 1.9
    },
    'Germany': {
        2022: 1.6,
        2023: 1.7,
        2024: 1.8
    },
    'United Kingdom': {
        2022: 1.2,
        2023: 1.3,
        2024: 1.4
    }
}

# Plotting the data
plt.figure(figsize=(12, 8))

for country, data in revenue_data.items():
    years = list(data.keys())
    revenue = list(data.values())
    plt.plot(years, revenue, marker='o', label=country)

# Adding titles and labels
plt.title('Top 5 Government Revenues Over Recent Years')
plt.xlabel('Year')
plt.ylabel('Revenue (in trillion USD)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
