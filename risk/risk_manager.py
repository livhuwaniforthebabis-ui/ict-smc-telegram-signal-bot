def calculate_lot(balance, risk_percent, stop_distance):

    risk_amount = balance * risk_percent

    lot = risk_amount / stop_distance

    return lot
