#!/usr/bin/env python3
from oneinch_py import OneInchSwap, TransactionHelper
import json, csv, sys, time
from decouple import config
from intial_setup import setup_rpc_url, Exiting, Check_Allowance, CheckBalance, GetBalance
from swap import Swap
from decimal import Decimal, ROUND_DOWN
from jsonpath_ng import jsonpath, parse


public_key = config('public_key')
# private_key = config('private_key')
investment_token = "USDC"

# if sys.argv[1] <= 1:
if len(sys.argv) <= 2:
    print("Usage: python get-token.py <blockchain>")
    print("Example: python get-token.py polygon")
    sys.exit(1)
chain = sys.argv[1]
rpc_url = setup_rpc_url(chain)
# tokens_list = sys.argv[2]
# percentage = sys.argv[3]

exchange = OneInchSwap(public_key, chain=chain) # initialise the OneInchSwap object as "exchange"
# helper = TransactionHelper(rpc_url, public_key, private_key, chain=chain) # initialise the TransactionHelper object as "helper"

tokens = exchange.get_tokens()
tokens = json.dumps(tokens, indent=4, sort_keys=True)
# print (tokens)

# Load the JSON data
# json_data = json.loads(json_string)
json_data = json.loads(tokens)

check=sys.argv[2]
# Use jsonpath-ng to access specific keys and values
jsonpath_expr = parse(f"$.{check}")

# Find the value of the 'symbol' key in the 'AGVE' object
matches = [match.value for match in jsonpath_expr.find(json_data)]

# Print the symbol for AGVE
if matches:
    print(json.dumps(matches[0]))
else:
    print(f"Symbol for {check} not found.")


exit(0)

# ./get-token.py polygon USDC | jq .
# {
#   "address": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174",
#   "decimals": 6,
#   "logoURI": "https://tokens.1inch.io/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.png",
#   "name": "USD Coin (PoS)",
#   "symbol": "USDC",
#   "tags": [
#     "tokens",
#     "PEG:USD"
#   ]
# }