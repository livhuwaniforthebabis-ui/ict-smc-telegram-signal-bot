import schedule
import time

from strategy.ict_smc_strategy import scan_markets
from bot.telegram_bot import send_analysis, send_signal
from tracker.trade_tracker import TradeTracker
from config import MAX_TRADES_PER_DAY

tracker = TradeTracker()


def run_signal_scan():

    if tracker.trades_today >= MAX_TRADES_PER_DAY:
        return

    setup = scan_markets()

    if setup is None:
        return

    send_analysis(setup)
    time.sleep(5)

    send_signal(setup)

    tracker.record_trade(setup)


schedule.every(5).minutes.do(run_signal_scan)

print("BOT RUNNING...")

while True:
    schedule.run_pending()
    time.sleep(1)
