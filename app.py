import requests
import tkinter as tk
def getData(cryptodata):
    response = requests.get(f"https://api.coinlore.net/api/tickers/{cryptodata.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()

    def search_function():
        search_request = search.get().lower()
        result = []

        for item in data:
            if search_request == item["name"].lower():
                result.append(f"{item['name'].lower()}")

        for i in range(0,99):
            name = data[i]["name"]
            symbol = data[i]["symbol"]
            price_usd = data[i]["price_usd"]
            percent_change_hour = data[i]["percent_change_1h"]
            coin_data = f"{name}: Symbol - {symbol}, Price (USD) - {price_usd}, Percent Change (HR) - ({percent_change_hour})"
            if result == data[i]["name"]:
                results_label.config(text=coin_data)
            else:
                results_label.config(text="No matches found.")

    """ name = data[0]["name"]
    symbol = data[0]["symbol"]
    price_usd = data[0]["price_usd"]
    percent_change_hour = data[0]["percent_change_1h"]

    name2 = data[1]["name"]
    symbol2 = data[1]["symbol"]
    price_usd2 = data[1]["price_usd"]
    percent_change_hour2 = data[1]["percent_change_1h"]
 """
    root = tk.Tk()
    root.title("Crypto Data")
    root.geometry("1280x780")


    label = tk.Label(root, text="Welcome to the crypto database! Find information about your most popular types of crypto by searching in the search bar", font=("Times New Roman", 14))
    label.pack(pady=10)

    search = tk.Entry(root, width=30, font=("Aerial", 14))
    search.pack(pady=10)

    search_button = tk.Button(root, text="Search", command=search_function, font=("Times New Roman", 14))
    search_button.pack(pady=5)

    results_label = tk.Label(root, text="", font=("Times New Roman", 14), justify="left")
    results_label.pack(pady=20)

    root.mainloop()
    
coin = getData("")
print(coin) 