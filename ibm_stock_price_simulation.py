
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate a date range from 1991 to 2023
date_range = pd.date_range(start="1991-01-01", end="2023-12-31", freq='B')  # 'B' stands for business day frequency

# Create a synthetic stock price series using random walk
np.random.seed(42)  # For reproducibility
stock_prices = np.round(100 + np.random.randn(len(date_range)).cumsum(), 2)

# Put the dates and stock prices into a DataFrame
ibm_stock_prices = pd.DataFrame({'Date': date_range, 'Stock_Price': stock_prices})

# Set the date as the index
ibm_stock_prices.set_index('Date', inplace=True)

# Plot the data
plt.figure(figsize=(14, 7))
plt.plot(ibm_stock_prices.index, ibm_stock_prices['Stock_Price'], label='IBM Stock Price')
plt.title('IBM Stock Price (1991 - 2023)')
plt.xlabel('Year')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
