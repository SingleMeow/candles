from indicators import exponential_MA
import plotly.graph_objects as go
from download_candles import download_candles
import plotly.express as px
import pandas as pd


df = download_candles('BBG004730N88')
df.to_csv('Данные торгов СБЕР 4 часа.csv')
