# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename: str, select: list = None, types: list = None, has_headers: bool = True, delimiter: str = ',', silence_errors = False) -> list:

    if (select and not has_headers):
        raise RuntimeError("Select argument requires column headers")
    records = []
    with open(filename) as f:
        rows = csv.reader(f, delimiter = delimiter)
        headers = next(rows) if has_headers else []

        if select:
            indexes = [headers.index(col) for col in select]
            headers = select

        for rn, row in enumerate(rows, start=1):
            if not row:
                continue
            if select:
                row = [row[i] for i in indexes]
            if types:
                try:
                    row = [func(col) for col, func in zip(row, types)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {rn}: Couldn't convert {row}")
                        print(f"Row {rn}: {e}")
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
    return records
            
l = parse_csv("Data/missing.csv", types = [str, int, float], silence_errors=True)
print(l)