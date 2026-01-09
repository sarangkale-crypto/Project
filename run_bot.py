import os
from basic_bot import BasicBot
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

def validate_side(side):
    side = side.upper()
    if side not in ("BUY", "SELL"):
        raise ValueError("Side must be BUY or SELL")
    return side

if __name__ == "__main__":
    bot = BasicBot(API_KEY, API_SECRET, testnet=True)

    try:
        symbol = input("Symbol (e.g., BTCUSDT): ").upper()
        side = validate_side(input("Side (BUY/SELL): "))
        quantity = float(input("Quantity: "))

        print("\n1. Market Order\n2. Limit Order\n3. Stop-Limit Order")
        choice = input("Choose order type: ")

        if choice == "1":
            order = bot.market_order(symbol, side, quantity)
        elif choice == "2":
            price = float(input("Limit Price: "))
            order = bot.limit_order(symbol, side, quantity, price)
        elif choice == "3":
            stop_price = float(input("Stop Price: "))
            limit_price = float(input("Limit Price: "))
            order = bot.stop_limit_order(symbol, side, quantity, stop_price, limit_price)
        else:
            print("Invalid choice")
            exit()

        print("\nOrder Placed Successfully")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")

    except Exception as e:
        print(f"\nError placing order: {e}")