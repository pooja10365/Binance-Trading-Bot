import os
import logging
from binance.client import Client
from binance.enums import *
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("TradingBot")

class BinanceClient:
    def __init__(self):
        api_key = os.getenv('BINANCE_API_KEY')
        api_secret = os.getenv('BINANCE_API_SECRET')
        self.client = Client(api_key, api_secret, testnet=True)
        logger.info("Binance Testnet Client Initialized")

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            params = {
                'symbol': symbol.upper(),
                'side': side.upper(),
                'type': order_type.upper(),
                'quantity': quantity,
            }
            
            # Logic for LIMIT and STOP_LIMIT
            if order_type.upper() in ['LIMIT', 'STOP_LIMIT']:
                params['price'] = str(price)
                params['timeInForce'] = TIME_IN_FORCE_GTC
            
            # Specific logic for the 3rd order type: STOP_LIMIT
            if order_type.upper() == 'STOP_LIMIT':
                if not stop_price:
                    raise ValueError("Stop Price is required for STOP_LIMIT orders")
                params['stopPrice'] = str(stop_price)

            logger.info(f"Sending Order: {params}")
            response = self.client.futures_create_order(**params)
            logger.info(f"Order Success: {response['orderId']}")
            return response
            
        except Exception as e:
            logger.error(f"Order Failed: {str(e)}")
            raise e
