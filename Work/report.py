# report.py
#
# Exercise 2.4

import csv
from pprint import pprint

def read_portfolio(filename: str, *, show_error = 1) -> list:
    '''
    Read portfolio csv file into a list of dictionaries (name, shares, price)
    '''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        # print(headers)
        for rn, row in enumerate(rows, start = 1):
            record = dict(zip(headers, row))
            try:
                name = record['name']
                nshares = int(record['shares'])
                price = float(record['price'])
            except ValueError as e:
                if show_error:
                    print('Bad data on row number:', rn, ', Error:', e)
                continue
            # holding = (name, nshares, price)
            holding = { 
                'name': name,
                'shares': nshares,
                'price': price
            }
            portfolio.append(holding)
    return portfolio

def read_prices(filename: str, *, show_error = 1) -> dict:
    '''
    Read a price file to a dictionary where keys are company names.
    '''
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for rn, row in enumerate(rows, start = 1):
            try:
                name = row[0]
                price = float(row[1])
            except IndexError as e:
                if show_error:
                    print('Bad data on row number:', rn, ', Error:', e)
                continue
            prices[name] = price
    return prices

def make_report(portfolio: list, prices: dict) -> list:
    '''
    Takes a portfolio list and prices dictionary as parameters and returns a list with difference beetwen original and current prices for each company
    '''
    report = []

    for row in portfolio:
        current_price = prices[row['name']]
        change = current_price - row['price']
        report_row = (row['name'], row['shares'], current_price, change)
        report.append(report_row)
    return report

def print_report(report: list) -> None:
    header = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % header)
    print(('-' * 10 + ' ') * len(header))
    [print(f"{row[0]:10s} {row[1]:10d} {'$' + str(round(row[2],2)):>10s} {row[3]:10.2f}") for row in report]
    return

def portfolio_report(portfolio_filename: str, prices_filename: str) -> None:
    portfolio = read_portfolio(portfolio_filename, show_error = 0)
    prices = read_prices(prices_filename, show_error=0)
    report = make_report(portfolio, prices)
    print_report(report)
    return

if __name__ == '__main__':
    portfolio_report('Data/portfolio.csv', 'Data/prices.csv')







