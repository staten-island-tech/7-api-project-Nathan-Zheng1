import requests
def getData(stockdata):
    response = requests.get(f"https://marketstack.com/?utm_source=Github&utm_medium=Referral&utm_campaign=Public-apis-repo-Best-sellers/{stockdata.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "price": data["price"],
    }
    
stock = getData("APPL")
print(stock) 
