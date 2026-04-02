import schedule
import time

from strategy.smc_strategy import scan_markets
from bot.telegram_bot import send_analysis, send_signal
from tracker.trade_tracker import TradeTracker
from config import MAX_TRADES_PER_DAY

tracker = TradeTracker()


def run_bot():

    if tracker.trades_today >= MAX_TRADES_PER_DAY:
        return

    setup = scan_markets()

    if not setup:
        return

    send_analysis(setup)

    send_signal(setup)

    tracker.record_trade(setup)


schedule.every(5).minutes.do(run_bot)

while True:
    schedule.run_pending()
    time.sleep(1)
