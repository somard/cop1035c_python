import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta

# Define the ticker symbol and time period for analysis
ticker_symbol = "XOM"
start_date = (datetime.now() - timedelta(days=10*365)).strftime('%Y-%m-%d')  # 10 years ago from today
end_date = datetime.now().strftime('%Y-%m-%d')

# Download historical data for Exxon Mobil
data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Reset the index to make 'Date' a column if it's not already one
data.reset_index(inplace=True)

# Calculate daily percentage change
data['Daily Change'] = data['Adj Close'].pct_change()

# Determine the trend of each day (Climbing if positive change, Slump if negative change)
data['Trend'] = np.where(data['Daily Change'] > 0, 'Climbing', 'Slump')

# Identify the start of a new period
data['Period Start'] = data['Trend'].ne(data['Trend'].shift()).cumsum()

# Correct the aggregation logic
period_summary = data.groupby(['Period Start']).agg(
    Start_Date=('Date', 'first'),
    End_Date=('Date', 'last'),
    Trend=('Trend', 'first'),  # Ensure 'Trend' is also aggregated correctly
    Duration=lambda x: (x.max() - x.min()).days
).reset_index(drop=True)

# Calculate average durations
average_climbing_duration = period_summary[period_summary['Trend'] == 'Climbing']['Duration'].mean()
average_slump_duration = period_summary[period_summary['Trend'] == 'Slump']['Duration'].mean()

print(f"Average Climbing Duration: {average_climbing_duration} days")
print(f"Average Slump Duration: {average_slump_duration} days")

