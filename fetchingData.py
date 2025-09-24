import yfinance as yf
import json 

class FetchData :

    def __init__(self, ticker):
        self.ticker = yf.Ticker(ticker)
        self.ticker_name = ticker
        # self.ticker =  yf.Ticker(ticker)

    def to_json(self , dict_ ):
        with open(f"{self.ticker_name.upper()}.json","w") as file:    
            pretty_json = json.dumps(dict_,indent=10)
            print(pretty_json)
            file.write(pretty_json)


    def userInput(self) :
        try:
            ticker = input("\npick the ticker you want to fetch (NVDA ,VIX ,QQQ... )")
            print(f"Ticker {ticker.upper()} is valid. Current price: {self.ticker.info['regularMarketPrice']}")
            # query_type = input("\nwhat kinde of data do you want (1- info , 2- calendar ,3- quarterly income statment 4- history based on the period 5 - fetch all: )")
            self.to_json(self.ticker.info)
        except Exception as e :
            print(e)


    



        # print(string_info)
FetchData("qqq").userInput()