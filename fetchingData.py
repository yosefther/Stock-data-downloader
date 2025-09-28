import yfinance as yf
import json
import pandas as pd
from pathlib import Path

class FetchData:
    def __init__(self, ticker_symbol: str, out_dir: str = "."):
        self.ticker_name = ticker_symbol.upper()
        self.ticker_obj = yf.Ticker(ticker_symbol)
        self.out_dir = Path(out_dir)
        self.out_dir.mkdir(parents=True, exist_ok=True)
    def _safe_filename(self, kind: str) -> str:
        return str(self.out_dir / f"{self.ticker_name}_{kind}.json")

    def _safe_csvname(self, kind: str) -> str:
        return str(self.out_dir / f"{self.ticker_name}_{kind}.csv")

    def _to_serializable(self, obj):
        if isinstance(obj, pd.DataFrame):
            return obj.reset_index().to_dict(orient="records")
        if isinstance(obj, pd.Series):
            return obj.to_dict()
        try:
            return dict(obj)
        except Exception:
            return str(obj)

    def to_json(self, data, kind: str):
        kind = kind.replace(" ", "_")
        filepath = self._safe_filename(kind)
        try:
            payload = self._to_serializable(data)
            pretty = json.dumps(payload, default=str, indent=4)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(pretty)
            print(f"Wrote JSON -> {filepath}")
        except Exception as e:
            print("Failed to write JSON:", e)

    def to_csv(self, data, kind: str):
        kind = kind.replace(" ", "_")
        filepath = self._safe_csvname(kind)
        try:
            if isinstance(data, pd.DataFrame):
                df = data.copy()
            elif isinstance(data, pd.Series):
                df = data.reset_index()
                df.columns = ["index", "value"]
            elif isinstance(data, dict):
                df = pd.DataFrame.from_dict(data, orient="index").reset_index()
            else:
                serial = self._to_serializable(data)
                df = pd.DataFrame(serial)
            df.to_csv(filepath, index=False)
            print(f"Wrote CSV -> {filepath}")
        except Exception as e:
            print("Failed to write CSV:", e)

    def clientInput(self):
        try:
            info = getattr(self.ticker_obj, "info", {}) or {}
            price = info.get("regularMarketPrice") or info.get("previousClose") or "N/A"
            print(f"Ticker {self.ticker_name} — Current price: {price}")

            query_type = input(
                "\nWhat kind of data would you like?\n"
                "1 - Metadata\n"
                "2 - Company Info (same as metadata in yfinance)\n"
                "3 - Calendar\n"
                "4 - Dividends\n"
                "5 - Earnings (try multiple fallbacks)\n"
                "6 - Analyst Price Targets / Recommendations\n"
                "7 - Quarterly Income Statement / Financials\n"
                "8 - Historical Data (choose period or dates)\n"
                "Enter your choice (1-8): "
            ).strip()

            if query_type == "1":
                self.to_json(info, "metadata")
                print(type(info))
            elif query_type == "2":
                self.to_json(info, "company_info")
                print(type(info))
            elif query_type == "3":
                calendar = getattr(self.ticker_obj, "calendar", None)
                self.to_json(calendar, "calendar")
                print(type(calendar))
            elif query_type == "4":
                dividends = getattr(self.ticker_obj, "dividends", None)
                if dividends is None or len(dividends) == 0:
                    print("No dividends found or series is empty.")
                else:
                    self.to_json(dividends, "dividends")
                    self.to_csv(dividends, "dividends")
                print(type(dividends))
            elif query_type == "5":
                earnings = None
                get_earnings = getattr(self.ticker_obj, "get_earnings", None)
                if callable(get_earnings):
                    try:
                        earnings = get_earnings()
                    except Exception:
                        earnings = None
                if not earnings:
                    earnings = getattr(self.ticker_obj, "earnings", None)
                if not earnings:
                    earnings = getattr(self.ticker_obj, "financials", None) or getattr(self.ticker_obj, "income_stmt", None)
                if earnings is None or (hasattr(earnings, "__len__") and len(earnings) == 0):
                    print("Earnings / income data not available via yfinance for this ticker (or deprecated).")
                else:
                    self.to_json(earnings, "earnings")
                    self.to_csv(earnings, "earnings")
                print("Type:", type(earnings))
            elif query_type == "6":
                apt = getattr(self.ticker_obj, "analyst_price_targets", None)
                recs = getattr(self.ticker_obj, "recommendations", None)
                if apt is not None and (not hasattr(apt, "__len__") or len(apt) > 0):
                    self.to_json(apt, "analyst_price_targets")
                    self.to_csv(apt, "analyst_price_targets")
                    print("Used analyst_price_targets attribute.")
                elif recs is not None and (not hasattr(recs, "__len__") or len(recs) > 0):
                    self.to_json(recs, "recommendations")
                    self.to_csv(recs, "recommendations")
                    print("Used recommendations attribute.")
                else:
                    print("No analyst price targets or recommendations available.")
            elif query_type == "7":
                q_fin = getattr(self.ticker_obj, "quarterly_financials", None) or getattr(self.ticker_obj, "quarterly_income_stmt", None) or getattr(self.ticker_obj, "quarterly_income_stmt", None)
                if q_fin is None or (hasattr(q_fin, "__len__") and len(q_fin) == 0):
                    q_fin = getattr(self.ticker_obj, "quarterly_financials", None)
                if q_fin is None or (hasattr(q_fin, "__len__") and len(q_fin) == 0):
                    print("Quarterly financials not available.")
                else:
                    self.to_json(q_fin, "quarterly_financials")
                    self.to_csv(q_fin, "quarterly_financials")
                print("Type:", type(q_fin))
            elif query_type == "8":
                choice = input("Fetch by (1) period (e.g. 1d,5d,1mo,1y,max) OR (2) start/end dates? Enter 1 or 2: ").strip()
                if choice == "1":
                    period = input("Enter period (e.g. 1d,5d,1mo,3mo,1y,5y,max): ").strip() or "1mo"
                    hist = self.ticker_obj.history(period=period)
                else:
                    start = input("Start date (YYYY-MM-DD): ").strip()
                    end = input("End date (YYYY-MM-DD) or leave blank for today: ").strip() or None
                    hist = self.ticker_obj.history(start=start, end=end)
                if hist is None or len(hist) == 0:
                    print("No historical data returned for that range/period.")
                else:
                    self.to_json(hist, f"historical_{choice}_{period if choice=='1' else start+'_'+(end or 'today')}")
                    self.to_csv(hist, "historical")
                print(type(hist))
            else:
                print("Invalid choice, please select a number from 1–8.")

        except Exception as e:
            print("An error occurred:", e)
