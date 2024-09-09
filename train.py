import yfinance as yf
from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np


# Download historical stock data
def download_stock_data(ticker='AAPL', period='5y'):
    stock_data = yf.download(ticker, period=period)
    stock_data['Return'] = stock_data['Close'].pct_change()  # Add return column
    return stock_data

stock_data = download_stock_data()


# Prepare data for LSTM
def prepare_lstm_data(stock_data, look_back=60):
    data = stock_data['Close'].values
    data = data.reshape(-1, 1)
    X, y = [], []
    for i in range(len(data) - look_back):
        X.append(data[i:i + look_back])
        y.append(data[i + look_back])
    return np.array(X), np.array(y)

X_train, y_train = prepare_lstm_data(stock_data)

# Define LSTM Model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(LSTM(units=50))
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=10, batch_size=32)
