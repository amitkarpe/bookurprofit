#!/usr/bin/env python3
from oneinch_py import OneInchSwap, TransactionHelper
import json, csv, sys, time
from decouple import config
from intial_setup import setup_rpc_url, Exiting, Check_Allowance, CheckBalance, GetBalance
# from swap import Swap
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
tokens_data = json.loads(tokens)
print (tokens_data)
exit (0)
# print (type (tokens_data))

token = sys.argv[2]
if token in tokens_data:
  # print(f"Token: {token}")
  # print(f"Symbol: {tokens_data[token]}")
  print(f"{json.dumps (tokens_data[token], indent=4, sort_keys=True)}")
  # print(f"Address: {tokens_data[token]['address']}")
  # decimal_places = tokens_data[token]['decimals']
  # print(f"Decimals: {tokens_data[token]['decimals']}")
else:
    print ("Token not found")

exit(0)

# export chain_id=100; curl -s https://api.1inch.io/v5.0/${chain_id}/tokens | jq '.tokens | to_entries[] | select(.value.symbol == "USDC") | .key'

# ./get-token2.py gnosis USDC | jq .
# {
#   "address": "0xddafbb505ad214d7b80b1f830fccc89b60fb7a83",
#   "decimals": 6,
#   "eip2612": true,
#   "logoURI": "https://tokens.1inch.io/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.png",
#   "name": "USD//C on xDai",
#   "symbol": "USDC",
#   "tags": [
#     "tokens"
#   ]
# }