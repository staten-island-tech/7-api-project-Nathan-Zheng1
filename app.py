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

    Bitcoin_data = f"Name: {name}, Symbol: {symbol}, Price (USD): {price_usd}"

    root = tk.Tk()
    root.title("Crypto Data")
    root.geometry("1280x780")

    def search_function():
        search_request = search.get().lower()
        result = []

        for item in data:
            if search_request == item["name"].lower():
                result.append(f"{item['name'].lower()}")

        if result == ["bitcoin"]:
            results_label.config(text=Bitcoin_data)
        else:
            results_label.config(text="No matches found.")

    label = tk.Label(root, text="Welcome to the crypto database! Find information about your most popular types of crypto by searching in the search bar", font=("Times New Roman", 14))
    label.pack(pady=10)

    search = tk.Entry(root, width=30, font=("Aerial", 14))
    search.pack(pady=10)

    search_button = tk.Button(root, text="Search", command=search_function, font=("Arial", 14))
    search_button.pack(pady=5)

    results_label = tk.Label(root, text="", font=("Arial", 14), justify="left")
    results_label.pack(pady=20)

    root.mainloop()
    
coin = getData("90")
print(coin) 