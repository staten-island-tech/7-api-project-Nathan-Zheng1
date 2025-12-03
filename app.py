import requests
import tkinter as tk
import json
def getData(cryptodata):
    response = requests.get(f"https://api.coinlore.net/api/ticker/?id={cryptodata.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()

    name = data[0]["name"]
    symbol = data[0]["symbol"]
    price_usd = data[0]["price_usd"]

    root = tk.Tk()
    root.title("Crypto Data")
    root.geometry("1280x780")

    search = tk.Entry(root)

    def search_function():
        search_request = search.get()



    Bitcoin_data = f"Name: {name}, Symbol: {symbol}, Price (USD): {price_usd}"

    label = tk.Label(root, text="Hello user! Click the button to view stocks", font=("Aerial", 14))
    label.pack(pady=10)

    def on_click():
        label.config(text="Bitcoin")
        label2 = tk.Label(root, text=Bitcoin_data, font=("Aerial", 14))
        label2.pack(pady=10)

    button = tk.Button(root, text="Click Me To Proceed", command=on_click)
    button.pack(pady=10)

    root.mainloop()
    
coin = getData("90")
print(coin) 