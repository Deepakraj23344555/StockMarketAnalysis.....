import numpy as np

def load_sample_data(stock):
    # Mock price range for selected stock
    base_price = {
        "RELIANCE": 2500,
        "INFY": 1500,
        "HDFCBANK": 1700
    }.get(stock, 2000)
    return np.linspace(base_price * 0.8, base_price * 1.2, 100)
