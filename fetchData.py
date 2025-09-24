import yfinance as yf
import json 

class FetchData :
    def __init__(self, ticker):
        self.ticker = ticker
        self.chosen_ticker =  yf.Ticker(ticker)
    def info(self):
        with open("QQQ.json","w") as file:    
            info_dict=self.chosen_ticker.info
            pretty_json = json.dumps(info_dict,indent=4)
            print(pretty_json)
            file.write(pretty_json)
        pass

    def userInput(self) :
        try:
            ticker = input("\npick the ticker you want to fetch (NVDA ,VIX ,QQQ... )")
            string_info = str(self.chosen_ticker.info).upper()
            print(f"Ticker {ticker} is valid. Current price: {self.chosen_ticker.info['regularMarketPrice']}")
            query_type = input("\nwhat kinde of data do you want (1- info , 2- calendar ,3- quarterly income statment 4- history based on the period 5 - fetch all: )")
            
            self.info()
            
            # test
            # if ("symbol" in info):
            #     with open(f"{ticker}.txt" , "a") as file:
            #         file.write(string_info)
            #     print(f"Ticker {ticker} is valid. Current price: {info['regularMarketPrice']}")

        except Exception as e :
            # print(f"Ticker {ticker} dose not seem valid or has no makret info  ")
            print(e)



        # print(string_info)
FetchData("qqq").userInput()