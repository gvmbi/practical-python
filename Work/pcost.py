#!/usr/bin/env python
# pcost.py

# Exercise 1.27

import csv
import sys
import report

# filename = 'Data/portfolio.csv'

def portfolio_cost_v1(filename: str) -> float:
    pcost: float = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        # headers: str = next(f).strip().split(',')
        headers = next(rows)
        # print(headers)
        for rowno, row in enumerate(rows, start = 1):
            # print(l, end = '')
            # row: list = l.strip().split(',')
            # print(row)
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                pcost += nshares  * price
            except ValueError:
                print(f'Row number: {rowno} Bad data: {row}')
    return pcost

def portfolio_cost(filename: str) -> float:
    portfolio = report.read_portfolio(filename)
    pcost = sum([row['shares'] * row['price'] for row in portfolio])
    print(f'Total cost: {pcost}')
    return pcost

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Bad parameters, usage: {argv[0]} portfolio_file')
    portfolio_cost(argv[1])

if __name__ == '__main__':
    main(sys.argv)
