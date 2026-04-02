import mplfinance as mpf
import MetaTrader5 as mt5
import pandas as pd

def generate_chart(symbol):

    rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M5, 0, 100)

    df = pd.DataFrame(rates)

    df['time'] = pd.to_datetime(df['time'], unit='s')

    df.set_index('time', inplace=True)

    filename = f"{symbol}_chart.png"

    mpf.plot(
        df,
        type='candle',
        style='charles',
        volume=False,
        savefig=filename
    )

    return filename
