# pcost.py
#
# Exercise 1.27

import csv
import sys

# filename = 'Data/portfolio.csv'

def portfolio_cost(filename: str) -> float:
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

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

pcost = portfolio_cost(filename)
print(f'Potfolio cost: {pcost}')