import time
import logging
from binance.client import Client

class BinanceBotClient:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret, testnet=True)
        self.client.API_URL = 'https://testnet.binancefuture.com/fapi'
        
        try:
            server_time = self.client.get_server_time()['serverTime']
            local_time = int(time.time() * 1000)
            self.client.timestamp_offset = server_time - local_time
        except Exception as e:
            print(f"Sync Error: {e}")

        self.logger = logging.getLogger(__name__)

    def test_connection(self):
        try:
            self.client.futures_account()
            self.logger.info("Successfully connected to Binance Futures Testnet")
            return True
        except Exception as e:
            self.logger.error(f"Connection Failed: {e}")
            return False