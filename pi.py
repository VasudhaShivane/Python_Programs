import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Download historical stock price data for Apple Inc. (AAPL) from Yahoo Finance
stock_symbol = 'AAPL'
start_date = '2020-01-01'
end_date = '2021-12-31'
data = yf.download(stock_symbol, start=start_date, end=end_date)

# Select the 'Close' price as the target variable
data = data[['Close']]

# Feature engineering (if desired)

# Create a new column 'Target' with the stock price shifted one day into the future
data['Target'] = data['Close'].shift(-1)

# Drop the last row with NaN values in the 'Target' column
data = data[:-1]

# Split the data into training and testing sets
X = data[['Close']]
y = data['Target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Model evaluation (e.g., MSE, RMSE)
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
print(f'Mean Squared Error (MSE): {mse:.2f}')
print(f'Root Mean Squared Error (RMSE): {rmse:.2f}')

# Plot actual vs. predicted prices
plt.figure(figsize=(12, 6))
plt.plot(data.index[-len(y_test):], y_test, label='Actual')
plt.plot(data.index[-len(y_test):], predictions, label='Predicted', linestyle='--')
plt.legend()
plt.title(f'Stock Price Prediction for {stock_symbol}')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.show()
