# Advanced Binance Futures Trading Bot (Testnet)

A robust, modular Python trading bot designed for the Binance Futures Testnet (USDT-M). This project demonstrates a clean separation between the API logic, a professional CLI, and a modern Web UI.

## 🌟 Key Features & Bonus Completions
- **Core Task:** Successful placement of MARKET and LIMIT orders.
- **Bonus 1 (Additional Order Type):** Added support for **STOP_LIMIT** orders.
- **Bonus 2 (Enhanced CLI UX):** Implemented an interactive terminal menu using `Questionary`.
- **Bonus 3 (Lightweight UI):** Developed a functional Web Dashboard using `Streamlit`.
- **Professional Logging:** All transactions are automatically logged to `logs/trading.log`.

## 🛠️ Installation
1. Clone the repository.
2. Create a `.env` file in the root directory and add your keys:
   ```text
   BINANCE_API_KEY=your_testnet_key
   BINANCE_API_SECRET=your_testnet_secret