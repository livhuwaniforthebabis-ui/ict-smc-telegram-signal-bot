import random
from config import PAIRS, CONFIDENCE_THRESHOLD


def detect_liquidity_sweep():
    return random.choice([True, False])


def detect_order_block():
    return random.choice([True, False])


def detect_fvg():
    return random.choice([True, False])


def scan_markets():

    pair = random.choice(PAIRS)

    liquidity = detect_liquidity_sweep()
    ob = detect_order_block()
    fvg = detect_fvg()

    score = 0

    if liquidity:
        score += 30

    if ob:
        score += 30

    if fvg:
        score += 30

    confidence = score

    if confidence < CONFIDENCE_THRESHOLD:
        return None

    direction = random.choice(["BUY", "SELL"])

    entry = round(random.uniform(100, 200), 2)

    if direction == "BUY":
        sl = entry - 3
        tp1 = entry + 4
        tp2 = entry + 8
    else:
        sl = entry + 3
        tp1 = entry - 4
        tp2 = entry - 8

    return {
        "pair": pair,
        "direction": direction,
        "bias": direction,
        "entry": entry,
        "sl": sl,
        "tp1": tp1,
        "tp2": tp2,
        "confidence": confidence
    }
