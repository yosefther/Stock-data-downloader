# note
You should refer to Yahoo!'s terms of use ([here](https://legal.yahoo.com/us/en/yahoo/terms/product-atos/apiforydn/index.html), [here](https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html), and [here](https://policies.yahoo.com/us/en/yahoo/terms/index.htm))  for details on your rights to use the actual data downloaded. 


#  Defining the project

### MVP
- Download historical data for one ticker.
- User specifies ticker + date range (hardcoded or simple input).
- Save results to a CSV file.
### core ideas 
- Support any ticker (not just one hardcoded).
- User can input date range and interval (daily, weekly, monthly).
- Save data in a structured format (CSV/Excel).
- Handle errors (e.g., invalid ticker).
### nice to have
Download multiple tickers at once.

- Save data to a database (SQLite, PostgreSQL, MongoDB).
- Add technical indicators (RSI, MACD, Bollinger Bands).
- Build a GUI (Tkinter, PyQt, Streamlit).
- Automate with a scheduler (download daily after market close).
- Support different APIs (Yahoo Finance, Alpha Vantage, Polygon).

#TODO
- [X]  fetch the symbole name form the info insted of the user input
- [X]  fix the naming system
- [X]  parsing text to json  (  Metadata /Company info /Calendar / Analyst price targets 'for small set'  )
- [ ]  parsing text to CSV (history ,dividends , earnings )
- [ ]  parsing text to SQL  (Historical OHLC data / Financial statements / Analyst price targets 'for bieggr sets'   )
