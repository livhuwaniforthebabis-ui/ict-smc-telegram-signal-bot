class TradeTracker:

    def __init__(self):

        self.trades_today = 0
        self.wins = 0
        self.losses = 0

    def record_trade(self, trade):

        self.trades_today += 1

    def record_win(self):

        self.wins += 1

    def record_loss(self):

        self.losses += 1

    def win_rate(self):

        total = self.wins + self.losses

        if total == 0:
            return 0

        return (self.wins / total) * 100
