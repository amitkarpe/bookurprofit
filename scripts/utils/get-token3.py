#!/usr/bin/env python3
from oneinch_py import OneInchSwap, TransactionHelper
import json, csv, sys, time
from decouple import config
from intial_setup import setup_rpc_url, Exiting, Check_Allowance, CheckBalance, GetBalance
from decimal import Decimal, ROUND_DOWN


public_key = config('public_key')
investment_token = "USDC"

chain = sys.argv[1]
rpc_url = setup_rpc_url(chain)

exchange = OneInchSwap(public_key, chain=chain) # initialise the OneInchSwap object as "exchange"
tokens = exchange.get_tokens()
tokens = json.dumps(tokens, indent=4, sort_keys=True)
tokens_data = json.loads(tokens)

if len(sys.argv) > 2:
    token = sys.argv[2]
else:
    token = "USDC"

token = token.upper()

decimal_places = tokens_data[token]['decimals']
print(decimal_places)

try:
    print(f"{json.dumps (tokens_data[token], indent=4, sort_keys=True)}")
except:
    error_message = {"error": f"Token '{token}' not found."}
    print(json.dumps(error_message, indent=4))
    # print(json.dumps({"error": f"Symbol for {token} not found."}, indent=4, sort_keys=True))
    exit(1)

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