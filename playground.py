from indicators import exponential_MA
import random as rd
import plotly.graph_objects as go

A = [i + 100 + (-1) ** (i + rd.randint(0, 1))  * rd.randint(1, 5) for i in range(150)]

EMA_1 = exponential_MA(A, 0.1)
print(EMA_1)
EMA_4 = exponential_MA(A, 0.4)
EMA_5 = exponential_MA(A, 0.5)
EMA_9 = exponential_MA(A, 0.7)

fig = go.Figure()
fig.add_trace(go.Scatter(y = A))
fig.add_trace(go.Scatter(y = EMA_1))
fig.add_trace(go.Scatter(y = EMA_4))
fig.add_trace(go.Scatter(y = EMA_5))
fig.add_trace(go.Scatter(y = EMA_9))
fig.show()