# 🤖 Binance Futures Automated CLI Trading Bot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Binance-Futures%20Testnet-F0B90B?style=for-the-badge&logo=binance&logoColor=black" alt="Binance" />
  <img src="https://img.shields.io/badge/Library-python--binance-343541?style=for-the-badge" alt="python-binance" />
  <img src="https://img.shields.io/badge/Order%20Types-MARKET%20%7C%20LIMIT-4CAF50?style=for-the-badge" alt="Order Types" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
</p>

A command-line automated trading interface engineered for **Binance USDⓈ-M Futures (Testnet)** using the official `python-binance` API wrapper. Built for algorithmic execution, this tool supports deterministic order dispatch (`MARKET` and `LIMIT`), automated NTP server timestamp synchronization, and structured audit logging.

---

## 🎯 Objective

Executing trades on cryptocurrency derivatives exchanges requires sub-millisecond precision, robust error handling, and auditability. 

**Binance-Trading-Bot** aims to:
- **Risk-Free Execution**: Leverage the official **Binance Futures Testnet** environment to test order routing strategies without risking real capital.
- **Clock Drift Mitigation**: Eliminate the notorious Binance API `-1021 TIMESTAMP` error by synchronizing local client execution timestamps directly against Binance server clocks.
- **Unified CLI Interface**: Provide algorithmic traders and developers with a simple, scriptable Command Line Interface (CLI) for rapid automated order placement.
- **Operational Audit Trails**: Persist all outbound requests, parameters, and server responses across simultaneous console and file handlers.

---

## ✨ Key Features

- **⚡ Order Types Supported**:
  - **`MARKET` Orders**: Immediate liquidity-taker fills at best available order book bid/ask.
  - **`LIMIT` Orders**: Maker/taker orders with enforced limit price parameter validation.
- **⏱️ Automated Timestamp Synchronization**:
  - Dynamically calculates offset between local system time and Binance Futures server time (`get_server_time`).
  - Seamlessly applies calculated timestamp offsets to prevent execution rejections.
- **📝 Comprehensive Logging Architecture**:
  - **Dual Handlers**: Real-time console terminal streaming (`StreamHandler`) combined with persistent file logging (`trading_bot.log`).
  - Formatted timestamps, log levels, module names, and transaction payloads.
- **🛡️ Parameter Sanitization & Safeguards**:
  - Validates order arguments prior to network dispatch.
  - Formats trading pairs into standardized uppercase ticker symbols (e.g., `BTCUSDT`, `ETHUSDT`).

---

## 🛠️ Tech Stack Used

| Component | Technology | Role |
|---|---|---|
| **Language** | Python 3.10+ | Execution runtime and CLI engine |
| **API Wrapper** | [`python-binance`](https://github.com/sammchardy/python-binance) | Official REST & WebSocket integration |
| **CLI Parser** | `argparse` | POSIX-compliant terminal argument parsing |
| **Audit Logging** | Python Standard `logging` | Synchronized dual-target event tracking |

---

## 📁 Repository Structure

```plaintext
binance-trading-bot/
├── binance_bot/
│   ├── cli.py             # Main CLI entrypoint and argument parser
│   ├── client.py          # Binance testnet client wrapper & time offset sync
│   ├── orders.py          # OrderManager abstraction for futures orders
│   ├── logging_config.py  # Centralized file & console logging configuration
│   ├── requirements.txt   # Required Python packages
│   └── trading_bot.log    # Local persistent transaction audit log
└── README.md              # Project documentation and setup guide
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/kunalnevage10-lgtm/binance-trading-bot.git
cd binance-trading-bot
```

### 2. Configure Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
cd binance_bot
pip install -r requirements.txt
```

### 4. Configure API Credentials
Create free credentials on the [Binance Futures Testnet](https://testnet.binancefuture.com/) and configure your keys in `binance_bot/cli.py` (or through environment variables):
```python
API_KEY = 'YOUR_BINANCE_TESTNET_API_KEY'
API_SECRET = 'YOUR_BINANCE_TESTNET_API_SECRET'
```

---

## 🚀 Usage Instructions

Navigate to the `binance_bot` directory and execute orders via the terminal:

### 1. Place a MARKET Buy Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

### 2. Place a MARKET Sell Order
```bash
python cli.py --symbol ETHUSDT --side SELL --type MARKET --quantity 0.05
```

### 3. Place a LIMIT Order (Price Required)
```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 62500.00
```

### 4. CLI Argument Reference
| Flag | Required | Values / Example | Description |
|---|---|---|---|
| `--symbol` | **Yes** | `BTCUSDT`, `ETHUSDT` | Target trading symbol |
| `--side` | **Yes** | `BUY`, `SELL` | Order direction |
| `--type` | **Yes** | `MARKET`, `LIMIT` | Order execution type |
| `--quantity` | **Yes** | `0.002` | Order lot size / volume |
| `--price` | *Limit Only* | `65000.50` | Limit execution price |

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE).
