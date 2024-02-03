#!/usr/bin/env python3


import warnings
import pandas as pd
from util import get_ticker_history, get_worksheet

environment = "dev"
# yfinance uses the 'unit' keyword from Pandas and for supressing it, the line below is necessary.
# Disable it on production
if environment == "dev":
    warnings.simplefilter(action="ignore", category=FutureWarning)


def pipeline(symbol: str):
    worksheet = get_worksheet(symbol)
    df = get_ticker_history(symbol)
    print(f"Writing data for {symbol}")
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print("Sucess")


def main():
    for s in ["META", "AMZN", "AAPL", "NFLX", "GOOG"]:
        pipeline(s)


if __name__ == "__main__":
    main()
