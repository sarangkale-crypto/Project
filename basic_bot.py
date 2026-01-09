from binance import Client
from binance.exceptions import BinanceAPIException
import logging
import os

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.logger = logging.getLogger(f"BasicBot_{id(self)}")
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            os.makedirs("logs", exist_ok=True)
            handler = logging.FileHandler("logs/trading_bot.log")
            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

        # Initialize Client with testnet=True
        self.client = Client(api_key, api_secret, testnet=testnet)
        
        # Override with NEW Spot Testnet URL (testnet.binance.vision is deprecated for trading)
        if testnet:
            self.client.API_URL = 'https://demo-api.binance.com/api'

        self.logger.info("Bot initialized for SPOT Testnet")

    def market_order(self, symbol, side, quantity):
        try:
            # CHANGED from futures_create_order to create_order (Spot)
            return self.client.create_order(
                symbol=symbol,
                side=side.upper(),
                type="MARKET",
                quantity=quantity
            )
        except Exception as e:
            self.logger.error("Market order failed: %s", e)
            raise

    def limit_order(self, symbol, side, quantity, price):
        try:
            return self.client.create_order(
                symbol=symbol,
                side=side.upper(),
                type="LIMIT",
                quantity=quantity,
                price=str(price),
                timeInForce="GTC"
            )
        except Exception as e:
            self.logger.error("Limit order failed: %s", e)
            raise