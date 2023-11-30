from indicators import exponential_MA
import random as rd
import plotly.graph_objects as go
from download_candles import download_candles

data = download_candles('BBG004730ZJ9')

data['EMA_1'] = exponential_MA(data['close'], 0.1)
data['EMA_4'] = exponential_MA(data['close'], 0.4)
data['EMA_5'] = exponential_MA(data['close'], 0.5)
data['EMA_7'] = exponential_MA(data['close'], 0.7)

fig = go.Figure()
fig.add_trace(go.Scatter(y = data['close']))
fig.add_trace(go.Scatter(y = data['EMA_1']))
fig.add_trace(go.Scatter(y = data['EMA_4']))
fig.add_trace(go.Scatter(y = data['EMA_5']))
fig.add_trace(go.Scatter(y = data['EMA_7']))
fig.show()