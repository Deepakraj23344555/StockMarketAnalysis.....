import pandas as pd
import plotly.graph_objects as go

def calculate_payoff(strategy, price_range, strike, premium, lot_size):
    df = pd.DataFrame({'Stock Price': price_range})
    if strategy == "Protective Put":
        df['Payoff'] = lot_size * (df['Stock Price'] - df['Stock Price']) + \
                       lot_size * (strike - df['Stock Price']).clip(lower=0) - premium * lot_size
    elif strategy == "Covered Call":
        df['Payoff'] = lot_size * (df['Stock Price'] - df['Stock Price']) - \
                       lot_size * (df['Stock Price'] - strike).clip(lower=0) + premium * lot_size
    elif strategy == "Collar":
        df['Payoff'] = (df['Stock Price'] - df['Stock Price']) + \
                       (strike - df['Stock Price']).clip(lower=0) - premium
    return df

def plot_payoff(df, strategy):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Stock Price'], y=df['Payoff'], mode='lines+markers', name=strategy))
    fig.update_layout(title=f"{strategy} Payoff Diagram", xaxis_title="Stock Price", yaxis_title="Net Payoff")
    st.plotly_chart(fig, use_container_width=True)
