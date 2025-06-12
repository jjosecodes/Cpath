


import pandas as pd





# Simulated DataFrames
stock_metadata = pd.DataFrame({
    'ticker': ['AAPL', 'GOOGL', 'MSFT', 'TSLA'],
    'company': ['Apple Inc.', 'Alphabet Inc.', 'Microsoft Corp.', 'Tesla Inc.'],
    'sector': ['Technology', 'Technology', 'Technology', 'Automotive']
})

stock_prices = pd.DataFrame({
    'ticker': ['AAPL', 'GOOGL', 'MSFT', 'TSLA'],
    'price': [195.34, 2805.67, 349.75, 230.89],
    'timestamp': [datetime.now().isoformat()] * 4
})