# ticker.py
from follow import follow
import csv
from report import read_portfolio
import tableformat

class Ticker:
    def __init__(self, name, price, change):
        self.name = name
        self.price = price
        self.change = change


def select_columns(rows, indexes):
    for row in rows:
        yield [row[ind] for ind in indexes]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        # yield {header:value for header, value in zip(headers, row)}
        yield dict(zip(headers, row))

def filter_names(rows, names):
    for row in rows:
        if row['Name'] in names:
            yield row

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['Name', 'Price', 'Change'])
    return rows

def ticker(portfile, logfile, fmt):
    lines = follow(logfile)
    portfolio = read_portfolio(portfile)
    rows = parse_stock_data(lines)
    rows = filter_names(rows, portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        formatter.row((row['Name'], str(row['Price']), str(row['Change'])))

if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    portfolio = read_portfolio('Data/portfolio.csv')
    rows = parse_stock_data(lines)
    rows = filter_names(rows, portfolio)
    for row in rows:
        print(row)