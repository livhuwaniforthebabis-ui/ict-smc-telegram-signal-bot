from tracker.trade_tracker import TradeTracker

tracker = TradeTracker()


def dashboard():

    winrate = tracker.win_rate()

    return f"""
📊 BOT DASHBOARD

Trades Today: {tracker.trades_today}

Wins: {tracker.wins}
Losses: {tracker.losses}

Win Rate: {winrate:.2f}%
"""
