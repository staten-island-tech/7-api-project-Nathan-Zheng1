import requests
import tkinter as tk
def getData(cryptodata):
    response = requests.get(f"https://api.coinlore.net/api/ticker/?id={cryptodata.lower()}")
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
                
            if result == ["bitcoin"]:
                results_label.config(text=f"Name: {name}({symbol}), Price: {price_usd}, Current Percent Change (1h): {percent_change_hour}")
            elif result == ["ethereum"]:
                results_label.config(text=f"Name: {name2}({symbol2}), Price: {price_usd2}, Current Percent Change (1h): {percent_change_hour2}")
            else:
                results_label.config(text="No matches found.")
    
    def load_game():
        label.config(text="Welcome to the triva gamemode! You will be tested on the history of bitcoin, please wait while it loads...", font=("Times New Roman", 14))
        questionnumber = []
        labelinfo.pack_forget()
        results_label.pack_forget()
        search.pack_forget()
        search_button.pack_forget()
        gamemode.pack_forget()

        question = tk.Label(root, wraplength=1024, text="1: During 2024, a certain event caused a huge increase in crypto hype and a overall stock market bull run. What was this event?", font=("Times New Roman", 14))
        question.pack(pady=40)

        questionnumber.append("1")

        inc1 = ["Incorrect Choice! You were close! This did cause a huge increase in crypto hype and a increase in crypto markets, but the impeltementation of crypto into the US Treasury was in majority passed in 2025, not 2024. Furthermore, this did not lead to a OVERALL market increase, but rather solely crpyto."]
        inc2 = ["This is correct! President Trump's election caused a huge uprise in the market! Buyers believed that his election would lead to huge gains, and bought tons of shares, propelling the market upward."]
        inc3 = ["Inncorrect Choice! In many occasions, it is true than markets are usually bullish after a 'long' bearish market, yet in 2024, there was no long period of bearish markets!"]
        inc4 = ["Incorrect Choice! New crypto coins typically do not ever cause the market, let alone the crypto market, to surge upwards. "]
        def incorrect_choice1():
            if questionnumber == ["1"]:
                choicelabel.config(text=inc1[0], wraplength=1024)
                answerchoice1.config(fg=("red"))
        def incorrect_choice2():
            if questionnumber == ["1"]:
                choicelabel.config(text=inc2[0], wraplength=1024)
                answerchoice2.config(fg=("Green"))
        def incorrect_choice3():
            if questionnumber == ["1"]:
                choicelabel.config(text=inc3[0], wraplength=1024)
                answerchoice3.config(fg=("red"))
        def incorrect_choice4():
            if questionnumber == ["1"]:
                choicelabel.config(text=inc4[0], wraplength=1024)
                answerchoice4.config(fg=("red"))

        choicelabel = tk.Label(root, text="", font=("Times New Roman", 14))
        answerchoice1 = tk.Button(root, width=30, wraplength=300, text=choice1[0], command=incorrect_choice1, justify=("center"), font=("Times New Roman", 14))
        answerchoice2 = tk.Button(root, width=30, wraplength=300, text=choice2[0], command=incorrect_choice2, justify=("center"), font=("Times New Roman", 14))
        answerchoice3 = tk.Button(root, width=30, wraplength=300, text=choice3[0], command=incorrect_choice3, justify=("center"), font=("Times New Roman", 14))
        answerchoice4 = tk.Button(root, width=30, wraplength=300, text=choice4[0], command=incorrect_choice4, justify=("center"), font=("Times New Roman", 14))
        choicelabel.pack(pady=10)
        answerchoice1.pack(pady=20)
        answerchoice2.pack(pady=20)
        answerchoice3.pack(pady=20)
        answerchoice4.pack(pady=20)

    choice1 = ["The possible implementation of crypto into the United States Treasury."]
    choice2 = ["The hype around the election of President Trump."]
    choice3 = ["It was the result of a enlongated period of a bearish market, propelled up back to a bullish market."]
    choice4 = ["The introduction of new crypto coins and the build-up of crypto hype."]

    name = data[0]["name"]
    symbol = data[0]["symbol"]
    price_usd = data[0]["price_usd"]
    percent_change_hour = data[0]["percent_change_1h"]

    name2 = data[1]["name"]
    symbol2 = data[1]["symbol"]
    price_usd2 = data[1]["price_usd"]
    percent_change_hour2 = data[1]["percent_change_1h"]

    root = tk.Tk()
    root.title("Crypto Data")
    root.geometry("1280x780")


    label = tk.Label(root, text="Welcome to the crypto database! Find information about your most popular types of crypto by searching in the search bar.", font=("Times New Roman", 14))
    label.pack(pady=25)

    labelinfo = tk.Label(root, text="Current Searchable Options: Bitcoin, Ethereum.")
    labelinfo.pack(pady=10)

    search = tk.Entry(root, width=30, font=("Aerial", 14))
    search.pack(pady=10)

    search_button = tk.Button(root, text="Search", command=search_function, font=("Times New Roman", 14))
    search_button.pack(pady=5)

    results_label = tk.Label(root, text="", font=("Times New Roman", 14), justify="left")
    results_label.pack(pady=20)

    gamemode = tk.Button(root, text="Triva!", command=load_game, font=("Times New Roman", 14))
    gamemode.pack(pady=50)


    root.mainloop()
    
coin = getData("90,80")
print(coin) 
