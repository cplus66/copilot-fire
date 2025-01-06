import twstock

# Define the stock ticker
ticker = '2395'  # Example: Taiwan Semiconductor Manufacturing Co Ltd (TSM)

# Manually set the stock name
stock_name = 'Advantech Co Ltd'

# Create a Stock object
stock = twstock.Stock(ticker)

# Fetch the latest stock price
latest_price = stock.price[-1]

# Print the latest stock price
print(f'Latest price of {stock_name}: {latest_price} TWD')

