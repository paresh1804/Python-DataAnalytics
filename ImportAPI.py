import requests

data=requests.get("https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol=BTC&market=EUR&apikey=R73DEFZ9W84OJYY8")
data2=data.json()
print(data.text)

print("===--===")

for p in data2["Time Series (Digital Currency Monthly)"]:
    print(p["5. volume"])