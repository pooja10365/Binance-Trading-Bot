import questionary
import sys
from bot.client import BinanceClient
from bot.logging_config import setup_logging

def main():
    setup_logging()
    print("\n🚀 Welcome to the Primetrade.ai Advanced Bot")
    
    symbol = questionary.text("Trading Pair:", default="BTCUSDT").ask()
    side = questionary.select("Side:", choices=["BUY", "SELL"]).ask()
    order_type = questionary.select("Order Type:", choices=["MARKET", "LIMIT", "STOP_LIMIT"]).ask()
    qty = questionary.text("Quantity:").ask()
    
    price = None
    stop_price = None
    
    if order_type in ["LIMIT", "STOP_LIMIT"]:
        price = questionary.text("Limit Price:").ask()
    if order_type == "STOP_LIMIT":
        stop_price = questionary.text("Stop Price:").ask()

    try:
        bot = BinanceClient()
        res = bot.place_order(symbol, side, order_type, float(qty), price, stop_price)
        print(f"\n✅ Success! Order ID: {res['orderId']}")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()