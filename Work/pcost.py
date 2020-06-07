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
        for row in rows:
            # print(l, end = '')
            # row: list = l.strip().split(',')
            # print(row)
            try:
                nshares = int(row[1])
                price = float(row[2])
                pcost += nshares  * price
            except ValueError:
                print('Row contains bad data -> skipped: ', row())
    return pcost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

pcost = portfolio_cost(filename)
print(f'Potfolio cost: {pcost}')