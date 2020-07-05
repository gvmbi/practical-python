import csv
from pprint import pprint
# with open('Data/portfoliodate.csv') as f:
#     rows = csv.reader(f)
#     headers = next(rows)
#     # print(headers)
#     select = ['name', 'shares', 'price']
#     indexes = [headers.index(cname) for cname in select]
#     l = [{cname : row[ind] for cname, ind in zip(headers, indexes)} for row in rows]
#     print(l)

# filename = 'Data/portfolio.csv'
# types = [str, int, float]

# converted =[]
# with open(filename) as f:
#     rows = f.readlines()
#     for row in rows:
#         l = row.strip().split(',')
#         try:
#             new_row = [ctype(cvalue) for cvalue,ctype in zip(l, types)]
#             converted.append(new_row)
#         except ValueError as e:
#             print(e)
# print(converted)         
def special_case(header, value, func):
    d = {}
    if header == 'date': 
        pass 
    else: 
        d[header] = func(value)
        return d

from datetime import datetime

filename = 'Data/dowstocks.csv'
converted = []
with open(filename) as f:
    rows = csv.reader(f)
    headers = next(rows)
    types = [str, float, str, str, float, float, float, float, int]
    print(headers)
    for row in rows:
        converted_row = { 
            header:
                (
                    tuple(int(d) for d in value.split('/')) if header == 'date' 
                    else func(value)
                ) 
                for header, value, func 
                in zip(headers, row, types)
            }
        converted.append(converted_row)
pprint(converted) 

