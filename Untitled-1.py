import requests
def getData(cryptodata):
    response = requests.get(f"https://api.coinlore.net/api/ticker/{cryptodata.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"]
    }
    
coin = getData("?id=90")
print(coin) 
