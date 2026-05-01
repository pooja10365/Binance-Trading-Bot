import streamlit as st
from bot.client import BinanceClient

st.set_page_config(page_title="Primetrade Trading Bot", page_icon="📈")
st.title("📈 Binance Futures Bot UI")

with st.sidebar:
    st.header("Order Settings")
    symbol = st.text_input("Symbol", value="BTCUSDT")
    side = st.selectbox("Side", ["BUY", "SELL"])
    order_type = st.selectbox("Type", ["MARKET", "LIMIT", "STOP_LIMIT"])
    qty = st.number_input("Quantity", min_value=0.001, step=0.001, format="%.3f")
    
    price = None
    stop_price = None
    if order_type in ["LIMIT", "STOP_LIMIT"]:
        price = st.number_input("Limit Price")
    if order_type == "STOP_LIMIT":
        stop_price = st.number_input("Stop Price")

if st.button("Place Order"):
    try:
        bot = BinanceClient()
        res = bot.place_order(symbol, side, order_type, qty, price, stop_price)
        st.success(f"Order Placed! ID: {res['orderId']}")
        st.json(res)
    except Exception as e:
        st.error(f"Error: {e}")