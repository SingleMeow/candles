import pandas as pd
import pytz
import time
import os 
from datetime import datetime, timedelta

from tinkoff.invest import CandleInterval, Client
from tinkoff.invest.utils import now

def download_candles(instrument_figi):

    os.environ["INVEST_TOKEN"] = "t.2Lq4ecGAavhC062SXymeQkDK6gdMa5tO-lnI5RMYsCKyLId4MkFEQoF5_wI0sqHNGp7-kCwAyvreG31eCWBF-A"
    TOKEN = os.environ["INVEST_TOKEN"]

    candle_intervals = {
    "1m": [CandleInterval.CANDLE_INTERVAL_1_MIN, "1 минута"],
    "2m": [CandleInterval.CANDLE_INTERVAL_2_MIN, "2 минуты"],
    "3m": [CandleInterval.CANDLE_INTERVAL_3_MIN, "3 минуты"],
    "5m": [CandleInterval.CANDLE_INTERVAL_5_MIN, "5 минут"],
    "10m": [CandleInterval.CANDLE_INTERVAL_10_MIN, "10 минут"],
    "15m": [CandleInterval.CANDLE_INTERVAL_15_MIN, "15 минут"],
    "30m": [CandleInterval.CANDLE_INTERVAL_30_MIN, "30 минут"],
    "1h": [CandleInterval.CANDLE_INTERVAL_HOUR, "1 час"],
    "2h": [CandleInterval.CANDLE_INTERVAL_2_HOUR, "2 часа"],
    "4h": [CandleInterval.CANDLE_INTERVAL_4_HOUR, "4 часа"],
    "1d": [CandleInterval.CANDLE_INTERVAL_DAY, "1 день"],
    "1w": [CandleInterval.CANDLE_INTERVAL_WEEK, "1 неделя"],
    "1M": [CandleInterval.CANDLE_INTERVAL_MONTH, "1 месяц"]}
    
    def window_select(interval):
        if interval in ('1m', '2m', '3m', '5m', '10m', '15m'):
            td = timedelta(days = 1)
        elif interval  == '30m':
            td = timedelta(days = 2)
        elif interval  == '1h':
            td = timedelta(days = 7)
        elif interval in ('2h', '4h'):
            td = timedelta(days = 30)
        elif interval == '1d':
            td = timedelta(days = 365)
        else:
            td = timedelta(days = 365*2)
        return td
    
    def create_df(candles):
        df = pd.DataFrame([{
            'time': c.time,
            'volume': c.volume,
            'open': cast_money(c.open),
            'close': cast_money(c.close),
            'high': cast_money(c.high),
            'low': cast_money(c.low),
        } for c in candles])
        return df

    def cast_money(v):
        r = v.units + v.nano / 1e9
        return r

    print('Please, select candle interval')
    
    for i in candle_intervals: print(i, candle_intervals[i])
    intval = input()
    td = window_select(intval)
    
    print('Please, provide starting date in form 31-12-20')
    
    start_dt = datetime.strptime(input(), "%d-%m-%y")
    start_dt = start_dt.replace(tzinfo=pytz.UTC)
    
    data = pd.DataFrame()
    
    with Client(TOKEN) as client:
        n_requests = 0
        while (start_dt < now()):

            data = pd.concat([data, create_df(client.get_all_candles(
                instrument_id = instrument_figi,
                from_ = start_dt,
                to = start_dt + td,
                interval = candle_intervals[intval][0]
            ))])

            start_dt = start_dt + td

            if n_requests <= 290:
                n_requests += 1
            else:
                n_requests = 0
                time.sleep(60)

        data = data.reset_index(drop = True)
        return data