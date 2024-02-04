#!/usr/bin/env python3

from typing import Optional
import yfinance as yf
import pandas as pd
import gspread


def symbol_to_ticker_history(symbol: str):
    return {
        "META": yf.Ticker("META"),
        "AMZN": yf.Ticker("AMZN"),
        "AAPL": yf.Ticker("AAPL"),
        "NFLX": yf.Ticker("NFLX"),
        "GOOG": yf.Ticker("GOOG"),
    }.get(symbol)


def get_ticker_history(symbol: str, ticker: yf.Ticker = None, period: str = "1y"):
    print(f"Getting ticker (symbol: {symbol}) history for the period of {period}.")
    ticker = symbol_to_ticker_history(symbol) if ticker is None else ticker
    r = ticker.history(period=period)
    print("Sucess.")
    return r


def sheet_to_gid(sheet: str) -> Optional[str]:
    return {
        "META": "1109944533",
        "AMZN": "1855112447",
        "AAPL": "68880361",
        "NFLX": "777146818",
        "GOOG": "1223970553",
    }.get(sheet)


def get_sheet():
    gc = gspread.service_account(filename=".gspread/service_account.json")
    return gc.open("Finance Source & View")


def get_worksheet(worksheet_title: str):
    sheet = get_sheet()
    return sheet.get_worksheet_by_id(sheet_to_gid(worksheet_title))


def get_worksheet_data(worksheet: gspread.Worksheet):
    worksheet.get("A:G")
    return worksheet
