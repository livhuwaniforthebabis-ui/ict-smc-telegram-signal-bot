from telegram import Bot
from config import TELEGRAM_TOKEN, VIP_GROUP_ID

bot = Bot(token=TELEGRAM_TOKEN)


def send_analysis(setup):

    text = f"""
📊 MARKET ANALYSIS

Pair: {setup['pair']}

Higher Timeframe Bias: {setup['bias']}

Timeframes Used
HTF: Daily / 4H
Confirmation: 1H / 15M
Entry: 5M

Reason For Setup

• Liquidity sweep
• Market structure shift
• Fair value gap
• Supply/Demand reaction

Confidence: {setup['confidence']}%
"""

    bot.send_message(chat_id=VIP_GROUP_ID, text=text)


def send_signal(setup):

    text = f"""
🚨 VIP TRADE SIGNAL 🚨

Pair: {setup['pair']}
Direction: {setup['direction']}

Entry: {setup['entry']}

Stop Loss: {setup['sl']}

Take Profit Targets

TP1: {setup['tp1']}
TP2: {setup['tp2']}

Risk: 1%
RR: 1:3
"""

    bot.send_message(chat_id=VIP_GROUP_ID, text=text)


def send_tp1(pair):

    bot.send_message(
        chat_id=VIP_GROUP_ID,
        text=f"""
✅ {pair} UPDATE

TP1 HIT

Stop Loss moved to Break Even
"""
    )


def send_tp2(pair):

    bot.send_message(
        chat_id=VIP_GROUP_ID,
        text=f"""
🏆 {pair}

TP2 HIT

Full target reached
"""
    )
