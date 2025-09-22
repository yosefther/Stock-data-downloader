import yfinance as yf

class StringToCsv:
    def __init__(self,string):
        self.string = string
    
    def parsing():
        print(self.string)


class DataType:
    def __init__(self , symbol):
        self.symbol = symbol 

    def Info(self):
        self.symbol = 4 
    def QuarterlyIncomeStat(self):
        print("")
    def calendar(self):
        print("")
    def FetchAll(self):
        print("")
    def History(self):
        print("")


if __name__ == "__main__":
    Data_Type =  DataType()
    try:
        ticker = input("\npick the ticker you want to fetch (NVDA ,VIX ,QQQ... )")
        chosen_ticker =  yf.Ticker(str(ticker))
        info = chosen_ticker.info 
        string_info = str(info).replace("," , "\n")
        if ("symbol" in info):
            with open("test_file.txt" , "a") as file:
                file.write(string_info)
            print(f"Ticker {ticker} is valid. Current price: {info['regularMarketPrice']}")
    except:
        print(f"Ticker {ticker} dose not seem valid or has no makret info  ")
        

    data_type = input("\nwhat kinde of data do you want (1- info , 2- calendar ,3- quarterly income statment 4- history based on the period 5 - fetch all  )")

    if(data_type == 1 ):
       Data_Type.Info(ticker) 
    elif(data_type == 2) : 
        Data_Type.calendar(ticker)
    elif(data_type == 3):
        Data_Type.QuarterlyIncomeStat(ticker)
    elif(data_type == 4):
        Data_Type.History(ticker)
    elif (data_type == 5 ):
        Data_Type.FetchAll(ticker)
  






