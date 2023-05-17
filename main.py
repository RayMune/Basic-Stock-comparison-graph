import yfinance as yf
import plotly.graph_objects as go

tesla = yf.Ticker('TSLA')
mercedes = yf.Ticker('MBG')  # updated ticker symbol for Mercedes
tesla_data = tesla.history(period='max')
mercedes_data = mercedes.history(period='max')

fig = go.Figure()

fig.add_trace(go.Scatter(x=tesla_data.index, y=tesla_data['Volume'], name='Tesla'))
fig.add_trace(go.Scatter(x=mercedes_data.index, y=mercedes_data['Volume'], name='Mercedes'))

fig.update_layout(title='Volume Comparison for Tesla and Mercedes Stocks')
fig.show()
