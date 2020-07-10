# report.py
#
# Exercise 2.4

import csv
import sys
from pprint import pprint
from fileparse import parse_csv

def read_portfolio_v1(filename: str, *, show_error = 1) -> list:
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

def read_portfolio(filename: str, silence_errors = False) -> list:
    with open(filename) as lines:
        portfolio = parse_csv(lines, select = ['name', 'shares', 'price'], types = [str, int, float], silence_errors = silence_errors)
        return portfolio

def read_prices_v1(filename: str, *, show_error = 1) -> dict:
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

def read_prices(filename: str, silence_errors = False) -> dict:
    with open(filename) as lines:
        prices = parse_csv(lines, types = [str, float], has_headers=False, silence_errors=silence_errors)
        return dict(prices)

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
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)
    return

def main(argv: list):
    if len(argv) != 3:
        raise SystemExit(f'Bad parameters, usage: {argv[0]} portfolio_file price_file')
    portfolio_report(argv[1], argv[2])

if __name__ == '__main__':
    main(sys.argv)
    # portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
    # l = read_portfolio('Data/portfolio.csv')
    # print(l)







