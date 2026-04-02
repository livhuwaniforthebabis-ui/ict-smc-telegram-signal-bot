from telegram import Bot
from config import TELEGRAM_TOKEN, VIP_GROUP_ID

bot = Bot(token=TELEGRAM_TOKEN)


def send_analysis(setup):

    msg = f"""
📊 MARKET ANALYSIS

Pair: {setup['pair']}

Bias: {setup['bias']}

Timeframes Used
HTF: Daily / 4H
Confirmation: 1H / 15M
Entry: 5M

Reason For Setup

• Liquidity sweep
• Order block reaction
• Fair Value Gap
• Market structure shift

Confidence: {setup['confidence']}%
"""

    bot.send_message(chat_id=VIP_GROUP_ID, text=msg)


def send_signal(setup):

    msg = f"""
🚨 VIP SIGNAL 🚨

Pair: {setup['pair']}
Direction: {setup['direction']}

Entry: {setup['entry']}

Stop Loss: {setup['sl']}

Take Profit

TP1: {setup['tp1']}
TP2: {setup['tp2']}

Risk: 1%
RR: 1:3
"""

    bot.send_message(chat_id=VIP_GROUP_ID, text=msg)


def send_tp1(pair):

    msg = f"""
✅ {pair} UPDATE

TP1 HIT

Stop Loss moved to Break Even
"""

    bot.send_message(chat_id=VIP_GROUP_ID, text=msg)


def send_tp2(pair):

    msg = f"""
🏆 {pair}

TP2 HIT

Full target reached
"""

    bot.send_message(chat_id=VIP_GROUP_ID, text=msg)
