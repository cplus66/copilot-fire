import matplotlib.pyplot as plt

# Data for government debt (in trillion USD)
debt_data = {
    'United States': {
        2022: 31.42,
        2023: 34,
        2024: 35
    },
    'Japan': {
        2022: 12.9,
        2023: 13.2,
        2024: 13.5
    },
    'China': {
        2022: 9.9,
        2023: 10.2,
        2024: 10.5
    },
    'Italy': {
        2022: 3.0,
        2023: 3.1,
        2024: 3.2
    },
    'Germany': {
        2022: 2.8,
        2023: 2.9,
        2024: 3.0
    }
}

# Plotting the data
plt.figure(figsize=(12, 8))

for country, data in debt_data.items():
    years = list(data.keys())
    debt = list(data.values())
    plt.plot(years, debt, marker='o', label=country)

# Adding titles and labels
plt.title('Top 5 Government Debts Over Recent Years')
plt.xlabel('Year')
plt.ylabel('Debt (in trillion USD)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
