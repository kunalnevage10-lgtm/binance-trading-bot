class OrderManager:
    def __init__(self, bot_client):
        self.client = bot_client.client

    def place_futures_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                'symbol': symbol.upper(),
                'side': side.upper(),
                'type': order_type.upper(),
                'quantity': float(quantity),
            }

            if order_type.upper() == 'LIMIT':
                if not price:
                    return {"error": "Price is required for LIMIT orders"}
                params['price'] = str(price)
                params['timeInForce'] = 'GTC' # Good Till Cancelled

            # Binance API call
            response = self.client.futures_create_order(**params)
            return response

        except Exception as e:
            return {"error": str(e)}