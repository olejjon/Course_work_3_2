import json
from datetime import datetime
from operator import itemgetter
import re

from funcs import sort_json, date_normal


# Основная функция вывода
def print_operations():
    data = sort_json()
    for operation in data[:5]:
        desc = operation['description']
        date = date_normal(operation['date'])
        if operation.get('from'):
            from_transfer = hide_number(operation['from'])
        to_transfer = card_account(operation['to'])
        summ = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']
        if operation.get('from'):
            print(f'{date} {desc}\n'
                  f'{from_transfer} -> {to_transfer}\n'
                  f'{summ} {currency}')
        else:
            print(f'{date} {desc}\n'
                  f'{to_transfer}\n'
                  f'{summ} {currency}')






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_operations()
