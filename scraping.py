import time

import bs4
import requests
import json
import pprint

url = 'https://www.idx.co.id/umbraco/Surface/Helper/GetStockChart?indexCode=SRTG&period=1W'
result = requests.get(url)
json_data = json.loads(result.text)
pprint.pprint(json_data)

#
# import datetime
# print(
#     datetime.datetime.fromtimestamp(
#         int("1543795200000")
#     ).strftime('%Y-%m-%d %H:%M:%S')
# )
#
# import dateutil.parser
# dateutil.parser.parse('1543795200000')

#https://stackoverflow.com/questions/19962249/timestamp-in-a-json-file
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int("1543795200000")/1000)))
