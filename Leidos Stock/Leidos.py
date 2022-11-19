import yfinance as yf
import streamlit as st

st.write("""
Simple Leidos Stock Application
""")

tickerSymbol = "LDOS"
tickerData = yf.Ticker(tickerSymbol)
tickerDF = tickerData.history(period='max')

st.write("""Closing Price""")
st.bar_chart(tickerDF.Close)

st.write("""Volume Price""")
st.bar_chart(tickerDF.Volume)

st.write("""Dividends""")
st.bar_chart(tickerDF.Dividends)
