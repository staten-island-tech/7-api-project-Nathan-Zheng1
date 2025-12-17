import requests
import tkinter as tk
def getData(cryptodata):
    response = requests.get(f"https://api.coinlore.net/api/tickers/?id={cryptodata.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()

    def search_function():
        search_request = search.get().lower()

        for item in data["data"]:
            if search_request == item["name"].lower():
                results_label.config(
                    text=(
                        f"Name: {item['name']} ({item['symbol']})"
                        f"Price: ${item['price_usd']}"
                        f"1h Change: {item['percent_change_1h']}%"
                    )
                )
            else:
                results_label.config(text="No matches found.")

    def question1():
        label.config(text="Welcome to triva! Select through the questions using the buttons.", font=("Times New Roman", 20))
        labelinfo.pack_forget()
        results_label.pack_forget()
        search.pack_forget()
        search_button.pack_forget()
        gamemode.pack_forget()

        questiontab1.pack(side="left", anchor="nw", padx=5)
        questiontab2.pack(side="left", anchor="nw", padx=5)
        questiontab3.pack(side="left", anchor="nw", padx=5)
        questiontab2.config(state="disabled")
        questiontab3.config(state="disabled")

        question.pack(pady=20)

        choicelabel.pack(pady=10)


        answerchoice11.pack(pady=20)
        answerchoice21.pack(pady=20)
        answerchoice31.pack(pady=20)
        answerchoice41.pack(pady=20)

    def question2():
        question.config(text="2: In the past, stock receipts were given _______.")

        choicelabel.config(text="")

        answerchoice11.pack_forget()
        answerchoice21.pack_forget()
        answerchoice31.pack_forget()
        answerchoice41.pack_forget()

        answerchoice12.pack(pady=20)
        answerchoice22.pack(pady=20)
        answerchoice32.pack(pady=20)
        answerchoice42.pack(pady=20)

    def question3():
        question.config(text="3: The storage crypto is typically held in is called: _______.")

        choicelabel.config(text="")


    def incorrect_choice1_1():
        choicelabel.config(text=inc1[0], wraplength=1024)
        answerchoice11.config(fg=("red"), state="disabled")
    def incorrect_choice2_1():
        choicelabel.config(text=inc2[0], wraplength=1024)
        answerchoice21.config(fg=("green"), bg="light green")
        questiontab2.config(state="normal")
        questiontab1.config(fg="green", bg="light green", state="disabled")
    def incorrect_choice3_1():
        choicelabel.config(text=inc3[0], wraplength=1024)
        answerchoice31.config(fg=("red"), state="disabled")
    def incorrect_choice4_1():
        choicelabel.config(text=inc4[0], wraplength=1024)
        answerchoice41.config(fg=("red"), state="disabled")

    def incorrect_choice1_2():
        choicelabel.config(text=inc1[1], wraplength=1024)
        answerchoice12.config(fg=("red"), state="disabled")
    def incorrect_choice2_2():
        choicelabel.config(text=inc2[1], wraplength=1024)
        answerchoice22.config(fg=("red"), state="disabled")
    def incorrect_choice3_2():
        choicelabel.config(text=inc3[1], wraplength=1024)
        answerchoice32.config(fg=("red"), state="disabled")
    def incorrect_choice4_2():
        choicelabel.config(text=inc4[1], wraplength=1024)
        answerchoice42.config(fg=("green"), bg="light green")
        questiontab2.config(state="disabled", fg="green", bg="light green")
    
    choice1 = ["The possible implementation of crypto into the United States Treasury.", "A form of a digital link which sends the buyer to his receipt statement."]
    choice2 = ["The hype around the election of President Trump.", "The receipt was sent via email instantly after purchase."]
    choice3 = ["It was the result of a enlongated period of a bearish market, propelled up back to a bullish market.", "A paper receipt which was mailed to the persons house after purchase of the stock."]
    choice4 = ["The introduction of new crypto coins and the build-up of crypto hype.", "A paper receipt given to the person directly after the purchase."]
    
    inc1 = ["Incorrect Choice! You were close! This did cause a huge increase in crypto hype and a increase in crypto markets, but the impeltementation of crypto into the US Treasury was in majority passed in 2025, not 2024. Furthermore, this did not lead to a OVERALL market increase, but rather solely crpyto.", "This is incorrect! In the early days of the stock market, technology didn't exist, and therefore digital receipts did not exit."]
    inc2 = ["This is correct! President Trump's election caused a huge uprise in the market! Buyers believed that his election would lead to huge gains, and bought tons of shares, propelling the market upward.", "This is incorrect! In the early days of the stock market, technology didn't exist, and therefore digital receipts did not exit."]
    inc3 = ["Inncorrect Choice! In many occasions, it is true than markets are usually bullish after a 'long' bearish market, yet in 2024, there was no long period of bearish markets!", "This is incorrect! While the receipt was given in paper, it was not mailed to the persons house."]
    inc4 = ["Incorrect Choice! New crypto coins typically do not ever cause the market, let alone the crypto market, to surge upwards.", "This is correct! After purchase of a stock, the broker would give you a paper which would act as a receipt."]

    root = tk.Tk()
    root.title("Crypto Data")
    root.geometry("1280x780")


    label = tk.Label(root, text="Welcome to the crypto database! Find information about your most popular types of crypto by searching in the search bar.", font=("Times New Roman", 18))
    label.pack(pady=25)

    question = tk.Label(root, wraplength=1024, text="1: During 2024, a certain event caused a huge increase in crypto hype and a overall stock market bull run. What was this event?", font=("Times New Roman", 14))

    choicelabel = tk.Label(root, text="", font=("Times New Roman", 14))

    answerchoice11 = tk.Button(root, width=30, wraplength=300, text=choice1[0], command=incorrect_choice1_1, justify=("center"), font=("Times New Roman", 14))
    answerchoice21 = tk.Button(root, width=30, wraplength=300, text=choice2[0], command=incorrect_choice2_1, justify=("center"), font=("Times New Roman", 14))
    answerchoice31 = tk.Button(root, width=30, wraplength=300, text=choice3[0], command=incorrect_choice3_1, justify=("center"), font=("Times New Roman", 14))
    answerchoice41 = tk.Button(root, width=30, wraplength=300, text=choice4[0], command=incorrect_choice4_1, justify=("center"), font=("Times New Roman", 14))
    answerchoice12 = tk.Button(root, width=30, wraplength=300, text=choice1[1], command=incorrect_choice1_2, justify=("center"), font=("Times New Roman", 14))
    answerchoice22 = tk.Button(root, width=30, wraplength=300, text=choice2[1], command=incorrect_choice2_2, justify=("center"), font=("Times New Roman", 14))
    answerchoice32 = tk.Button(root, width=30, wraplength=300, text=choice3[1], command=incorrect_choice3_2, justify=("center"), font=("Times New Roman", 14))
    answerchoice42 = tk.Button(root, width=30, wraplength=300, text=choice4[1], command=incorrect_choice4_2, justify=("center"), font=("Times New Roman", 14))

    questiontab1 = tk.Button(root, text="1", command=question1, font=("Times New Roman", 20))
    questiontab2 = tk.Button(root, text="2", command=question2, font=("Times New Roman", 20))
    questiontab3 = tk.Button(root, text="3", command=question3, font=("Times New Roman", 20))

    labelinfo = tk.Label(root, text="Current Searchable Options: Bitcoin, Ethereum.")
    labelinfo.pack(pady=10)

    search = tk.Entry(root, width=30, font=("Aerial", 14))
    search.pack(pady=10)

    search_button = tk.Button(root, text="Search", command=search_function, font=("Times New Roman", 14))
    search_button.pack(pady=5)

    results_label = tk.Label(root, text="", font=("Times New Roman", 14), justify="left")
    results_label.pack(pady=20)

    gamemode = tk.Button(root, text="Triva!", command=question1, font=("Times New Roman", 14))
    gamemode.pack(pady=50)


    root.mainloop()
    
coin = getData("90,80")
print(coin) 
