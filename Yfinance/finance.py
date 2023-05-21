import yfinance as yf

msft = yf.Ticker("MSFT")

msft.info

hist = msft.history(period="max")

print(hist)