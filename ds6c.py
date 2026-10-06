import pandas as pd
india_dates=pd.date_range(
    start='2026-07-21 06:00',
    periods=3,
    freq='h',
    tz='Asia/Kolkata'
)
print("1. Date Range with Asia/Kolkata Time zone:")
print(india_dates)
dates