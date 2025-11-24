import requests
def getData(cryptodata):
    response = requests.get(f"https://www.coinlore.com/cryptocurrency-data-api/{cryptodata.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "Market Cap": data["Market Cap"]
    }
    
coin = getData("Bitcoin")
print(coin) 
