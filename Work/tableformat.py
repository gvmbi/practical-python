# tableformat.py

class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end = ' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for row in rowdata:
            print(f'{row:>10s}', end = ' ')
        print()


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))
        
    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end = '')
        for h in headers:
            print(f'<th>{h}</th>', end = '')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end = '')
        for r in rowdata:
            print(f'<td>{r}</td>', end = '')
        print('</tr>')

def create_formatter(fmt):
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format: {fmt}')
    return formatter

def print_table(portfolio, attr_list, formatter):
    formatter.headings(attr_list)

    for row in portfolio:
        filtered_row = [str(getattr(row, attr)) for attr in attr_list]
        formatter.row(filtered_row)
