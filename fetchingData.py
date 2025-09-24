import yfinance as yf
import json 

class FetchData :


    def __init__(self, ticker_obj):
        self.ticker_obj = yf.Ticker(ticker_obj)
        self.ticker_name = ticker_obj
        # self.ticker_obj =  yf.Ticker(ticker_obj)

    def to_json(self , dict , type ):
        with open(f"{self.ticker_name.upper()}_{type}.json","w") as file:    
            pretty_json = json.dumps(dict,default=str,indent=4)
            print(pretty_json)
            file.write(pretty_json)

    def to_csv():
        pass

    def clientInput(self) :
        try:
            print(f"Ticker {self.ticker_name.upper()} is valid. Current price: {self.ticker_obj.info['regularMarketPrice']}")
            query_type = input("\nWhat kind of data would you like?\n"
            "1 - Metadata\n"
            "2 - Company Info\n"
            "3 - Calendar\n"
            "4 - Dividends\n"
            "5 - Earnings\n"
            "6 - Analyst Price Targets\n"
            "7 - Quarterly Income Statement\n"
            "8 - Historical Data (by period)\n"
            "Enter your choice (1-9): ")
            if query_type == "1":
                # Metadata
                self.to_json(self.ticker_obj.info, "metadata")
                print(type(self.ticker_obj.info))
            elif query_type == "2":
                # Company Info
                self.to_json(self.ticker_obj.info, "company_info")
                print(type(self.ticker_obj.info))
            elif query_type == "3":
                # Calendar
                self.to_json(self.ticker_obj.calendar, "calendar")
                print(type(self.ticker_obj.calendar))
            elif query_type == "4":
                # Dividends
                # CSV
                pass
            elif query_type == "5":
                # Earnings
                # self.to_json(self.ticker_obj.dividends, "test")
                print(type(self.ticker_obj.dividends))
                #TODO : fix
                # ``` 
                #     self.to_json(self.ticker_obj.earnings, "earnings")
                #     print(type(self.ticker_obj.earnings))
                # ```
                # error
                    #  DeprecationWarning: 'Ticker.earnings' is deprecated as not available via API. Look for "Net Income" in Ticker.income_stmt.
                    #   warnings.warn("'Ticker.earnings' is deprecated as not available via API. Look for \"Net Income\" in Ticker.income_stmt.", DeprecationWarning)
                    # null
                    # <class 'NoneType'>

                pass
            elif query_type == "6":
                # Analyst Price Targets
                self.to_json(self.ticker_obj.analyst_price_targets, "analyst_price_targets")
                print(type(self.ticker_obj.analyst_price_targets))
            elif query_type == "7":
                # Quarterly Income Statement
                # CSV
                pass
            elif query_type == "8":
                # Historical Data (by period)
                # CSV
                pass
            
            # elif query_type == "9":
            #     # Fetch All
            #     print("Fetched all data.")
            
            else:
                print(" Invalid choice, please select a number from 1–8.")






            # self.to_json(self.ticker_obj.info)
        
        except Exception as e :
            print(e)


    



# test

FetchData("nvda").clientInput()