import yfinance as yf
# dat = yf.Ticker("MSFT")
# print(dat.calendar)
# print(dat.info)
# print(dat.analyst_price_targets) add latter 
# print(dat.quarterly_income_stmt)
# print(dat.history(period='1mo'))

class DataType:
    def Info(self,symbol):
        print("")
    def QuarterlyIncomeStat(self,symbol):
        print("")
    def calendar(self,symbol):
        print("")
    def FetchAll(self,symbol):
        print("")
    def History(self,symbol):
        print("")



if __name__ == "__main__":
    Data_Type =  DataType()
    try:
        ticker = input("\npick the ticker you want to fetch (NVDA ,VIX ,QQQ... )")
        chosen_ticker =  yf.Ticker(str(ticker))
        info = chosen_ticker.info 
        if ("symbol" in info):
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





# todo : fetch the symbole name form the info insted of the user input   
# todo : fox the naming system 
 
# try:
#     chosen_ticker = yf.Ticker(ticker)
#     # Try fetching some data to make sure the ticker exists
#     info = chosen_ticker.info
#     if 'regularMarketPrice' in info:
#         print(f"Ticker {ticker} is valid. Current price: {info['regularMarketPrice']}")
#     else:
#         print(f"Ticker {ticker} does not seem valid or has no market data.")
# except Exception as e:
#     print("Error fetching ticker:", e)


