import requests
import tkinter as tk
def getData(cryptodata):
    response = requests.get(f"https://api.coinlore.net/api/ticker/?id={cryptodata.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data[0]["name"],
        "symbol": data[0]["symbol"],
        "price_usd": data[0]["price_usd"]
    }
    
coin = getData("90")
print(coin) 

root = tk.Tk()
root.title("Crypto Data")
root.geometry("450x150")

label = tk.Label(root, text="Hello user! Click the button to view stocks")
label.pack(pady=10)

def on_click():
    label.config(text="Bitcoin")

button = tk.Button(root, text="Click Me", command=on_click)
button.pack(pady=10)

root.mainloop()