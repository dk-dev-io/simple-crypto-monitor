#Bitcoin Price Monitor & Failover Bot

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/Status-Active-green)

A resilient background service for monitoring Bitcoin prices with built-in redundancy, logging, and automated trading advice logic.

##Key Features

* **Redundancy (Failover):** Uses **CoinDesk API** as the primary source. If it fails or becomes unreachable, the script automatically switches to **CoinGecko API** to ensure continuous data flow.
* **Logging System:** * `price_history.txt`: Records successful price fetches with timestamps.
    * `errors.txt`: Logs connectivity issues and API failures for debugging.
* **Automated Analysis:** Real-time price evaluation to generate simple trading signals (BUY/SELL) based on defined thresholds.
* **Daemon-like Behavior:** Designed to run continuously as a background process with smart delays to respect API rate limits.

##How It Works

1.  **Fetch:** Attempts to get the current BTC/USD rate from the primary API.
2.  **Fallback:** If an exception occurs (network error, timeout, 500 status), it seamlessly triggers the backup API logic.
3.  **Log:** Saves the result or specific error details to the local file system.
4.  **Analyze:** Compares the current rate against the threshold (e.g., $90,000) and prints advice to the console.

##Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/dk-dev-io/simple-crypto-monitor.git
    cd crypto-monitor
    ```

2.  **Install requirements:**
    This script uses the `requests` library.
    ```bash
    pip install requests
    ```

3.  **Run the monitor:**
    ```bash
    python main.py
    ```

##Technology Stack

* **Python 3**
* **Requests** (HTTP Client)
* **JSON Parsing**
* **File I/O** (Logging)

##Future Improvements
* Add Telegram Bot integration for push notifications.
* Implement asynchronous requests (`asyncio`) for faster polling.
* Dockerize the application for easy deployment.