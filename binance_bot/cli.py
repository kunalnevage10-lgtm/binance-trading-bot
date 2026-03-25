import argparse
import logging
from logging_config import setup_logging
from client import BinanceBotClient
from orders import OrderManager

# 1. API Keys yahan dalo (Notepad se copy karke)
API_KEY = 'aoQx5nSWlMX62GS9wqWCXXgGb0IwWtF8vrP3cOg6MhOwjXDU3tuVy8JGlCUHjz4i'
API_SECRET = 'bb8PQGGxR2Pt0W9PE7VfCu9LVxUJB7DRDaDOx5EzTcrAC41TEOfy86iKX7W7RfPI'

def main():
    # Logging setup
    setup_logging()
    logger = logging.getLogger(__name__)

    # CLI Arguments setup
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot CLI")
    parser.add_argument('--symbol', type=str, required=True, help="e.g. BTCUSDT")
    parser.add_argument('--side', type=str, required=True, choices=['BUY', 'SELL'])
    parser.add_argument('--type', type=str, required=True, choices=['MARKET', 'LIMIT'])
    parser.add_argument('--quantity', type=float, required=True)
    parser.add_argument('--price', type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    # Client initialize karo
    bot_client = BinanceBotClient(API_KEY, API_SECRET)
    
    # Connection test karo
    if not bot_client.test_connection():
        return

    # Order manager initialize karo
    manager = OrderManager(bot_client)

    # Order request summary print karo (Requirement)
    print(f"\n--- Order Request Summary ---")
    print(f"Symbol: {args.symbol}, Side: {args.side}, Type: {args.type}, Qty: {args.quantity}")
    if args.price: print(f"Price: {args.price}")
    print("-----------------------------\n")

    # Order place karo
    response = manager.place_futures_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    # Response Handle karo
    if "error" in response:
        logger.error(f"Order Failed: {response['error']}")
    else:
        logger.info(f"Order Success! ID: {response['orderId']}, Status: {response['status']}")
        print(f"\n--- Order Response Details ---")
        print(f"OrderID: {response['orderId']}")
        print(f"Status: {response['status']}")
        print(f"Executed Qty: {response.get('executedQty', '0')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")
        print("------------------------------")

if __name__ == "__main__":
    main()