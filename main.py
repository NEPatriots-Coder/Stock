import streamlit as st          
import yfinance as yf          
                                
                                
st. title("Doosan Stock Price Analysis")
st.write("""### ***All information provided by Yahoo Finance***""")
st.write(""" ## Stock Price of Doosan Corp
Shown is *Opening Price*, *Closing Price*, and *Daily Volume*""")

tickerSymbol = "000150.KS"
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2018-01-01', end='2023-10-04')

                                
st.write("## Opening Price")    
st.line_chart(tickerDf.Open)    
st.write("## Closing Price")    
st.line_chart(tickerDf.Close)  
st.write("## Daily Volume")
st.line_chart(tickerDf.Volume) 

Bobcat = yf.Ticker("000150.KS")
Bobcat.info 

st.write("### The following will list a few summary statistics about Doosan Bobcat")
Bobcat.actions
Bobcat.dividends
Bobcat.splits
Bobcat.capital_gains


Bobcat.major_holders

Bobcat.earnings_dates
st.write("## Doosan Income Statement")
Bobcat.income_stmt
st.write("## Doosan Balance Sheet")
Bobcat.balancesheet
st.write("## Doosan Cash Flow")
Bobcat.cashflow

hist = Bobcat.history