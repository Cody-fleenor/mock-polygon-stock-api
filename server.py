#!/usr/bin/env python
# encoding: utf-8
import json
from urllib import response
from flask import Flask, request, jsonify
app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def query_records():
#     name = request.args.get('name')
#     with open('/tmp/data.txt', 'r') as f:
#         data = f.read()
#         records = json.loads(data)
#         for record in records:
#             if record['name'] == name:
#                 return jsonify(record)
#         return jsonify({'error': 'data not found'})


# ========== Stocks Mock Market Data End Points =================
agg_response = {
 "adjusted": True,
 "queryCount": 2,
 "request_id": "6a7e466379af0a71039d60cc78e72282",
 "results": [
  {
   "c": 75.0875,
   "h": 75.15,
   "l": 73.7975,
   "n": 1,
   "o": 74.06,
   "t": 1577941200000,
   "v": 135647456,
   "vw": 74.6099
  },
  {
   "c": 74.3575,
   "h": 75.145,
   "l": 74.125,
   "n": 1,
   "o": 74.2875,
   "t": 1578027600000,
   "v": 146535512,
   "vw": 74.7026
  }
 ],
 "resultsCount": 2,
 "status": "OK"
}

tickOpenClose = {
 "afterHours": 322.1,
 "close": 325.12,
 "from": "2020-10-14T00:00:00.000Z",
 "high": 326.2,
 "low": 322.3,
 "open": 324.66,
 "preMarket": 324.5,
 "status": "OK",
 "symbol": "AAPL",
 "volume": 26122646
}

@app.route('/')
def hello_world():
    return 'Hello World!'

trustedKeys = ['1000000']

@app.route('/v2/aggs/ticker/<ticker>/range/<multiplier>/<timespan>/<date_from>/<date_to>/<key>', methods=['GET'])
def stockAggregator(ticker, multiplier, timespan, date_from, date_to, key):
    if key in trustedKeys:
        agg_response.__setitem__('ticker', ticker)
        response = agg_response
        print(ticker, multiplier, timespan, date_from, date_to)
    else:
        response = "invalid key"
    return jsonify(response)

@app.route('/v2/aggs/grouped/locale/us/market/stocks/<date>/<key>', methods=['GET'])
def marketAggregator(date, key):
    if key in trustedKeys:
        agg_response.__delitem__('ticker')
        response = agg_response
        print(date)
    else:
        response = "invalid key"
    return jsonify(response)

@app.route('/v1/open-close/<ticker>/<date>/<key>', methods=['GET'])
def dailyOpenClose(ticker, date, key):
    if key in trustedKeys:
        tickOpenClose.__setitem__('symbol', ticker)
        tickOpenClose.__setitem__('from', date)
        response = agg_response
    else:
        response = "invalid key"
    return jsonify(response)
# ========== Stocks Reference End Points ================= 


# ========== Stocks Webhook End Points =================



if __name__ == '__main__':
    app.run(debug=True)