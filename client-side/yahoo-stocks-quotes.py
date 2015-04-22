# download stocks quotes in csv

import requests
import time

i = 0
stock_list = ['GOOG', 'YHOO', 'AOL']

while (i < 1):
    print 'test'
    base_url = 'http://download.finance.yahoo.com/d/quotes.csv'
    for stock in stock_list:
        data = requests.get(base_url,
                            params={'s': stock,
                                    'f': 'sl1d1t1c1ohgv',
                                    'e': '.csv'})

        with open("stocks.csv", "a") as code:
            code.write(data.content)
    i += 1

    time.sleep(3)
