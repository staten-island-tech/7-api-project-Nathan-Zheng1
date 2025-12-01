import requests
def getData(cryptodata):
    response = requests.get(f"https://api.coinlore.net/api/ticker/?id={cryptodata.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "symbol": data["symbol"],
        "price_usd": data["price_usd"]
    }
    
coin = getData("90")
print(coin)