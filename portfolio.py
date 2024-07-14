# -*- coding: utf-8 -*-
"""Stock Portfolio Tracker.ipynb"""

import requests

class Portfolio:
    def __init__(self):
        self.portfolio = {}

    def add(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity

    def remove(self, symbol, quantity):
        if symbol in self.portfolio:
            if self.portfolio[symbol] >= quantity:
                self.portfolio[symbol] -= quantity
                if self.portfolio[symbol] == 0:
                    del self.portfolio[symbol]
            else:
                print("Error: Quantity to remove exceeds available shares.")
        else:
            print("Error: Stock symbol not found in portfolio.")

    def get_portfolio(self):
        total_value = 0
        for symbol, quantity in self.portfolio.items():
            price = self.get_stock_price(symbol)
            if price:
                total_value += price * quantity
        return total_value

    def get_price(self, symbol):
        api_key = 'CR2MH27GP2DX9B6I'
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
        response = requests.get(url)
        data = response.json()
        if 'Global Quote' in data:
            return float(data['Global Quote']['05. price'])
        else:
            print("Error: Unable to retrieve stock price.")
            return None

# Example usage
portfolio = StockPortfolio()
portfolio.add('Python', 10)
portfolio.add('Program', 5)
portfolio.add('Ml', 7)

print("Portfolio Value:", portfolio.get_portfolio())
portfolio.remove('AAPL', 5)
print("Portfolio Value:", portfolio.get_portfolio())
