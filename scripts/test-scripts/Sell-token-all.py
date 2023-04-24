# Sell-token-all.py

from oneinch_py import OneInchSwap, TransactionHelper
import json csv
from decouple import config
from os import system
import sys
from intial_setup import setup_rpc_url, Exiting, Check_Allowance, CheckBalance, GetBalance
from swap import Swap
from decimal import Decimal, ROUND_DOWN

# pip install python-decouple 1inch.py==1.8.2 requests==2.28.1 web3<6.0
public_key = config('public_key')
private_key = config('private_key')


# if len(sys.argv) != 5:
#     print("Usage: python Buy-token.py <blockchain> <investment token> <buy token> <buying amount with decimal>")
#     print("Example: python Buy-token.py polygon USDC QUICK 0.0001")
#     sys.exit(1)


# chain = sys.argv[1]
# rpc_url = setup_rpc_url(chain)
# investment_token = sys.argv[2]
# token = sys.argv[3]
# amount = float(sys.argv[4])

# print("Investment Token:", investment_token)
# print("Buy Token:", token)
# print("Buying Amount:", amount)

chain = "gnosis"
rpc_url = setup_rpc_url(chain)

exchange = OneInchSwap(public_key, chain=chain) # initialise the OneInchSwap object as "exchange"
helper = TransactionHelper(rpc_url, public_key, private_key, chain=chain) # initialise the TransactionHelper object as "helper"

tokens = exchange.get_tokens()
print (type (tokens))
# conver token into json format and print
# print (json.dumps(tokens, indent=4, sort_keys=True))
tokens = json.dumps(tokens, indent=4, sort_keys=True)
print (type (tokens))
# print first token symbol
json_string = tokens
tokens_data = json.loads(json_string)

agve_symbol = tokens_data["AGVE"]["symbol"]
selected_tokens = ["AGVE", "WBTC", "WETH", "USDC", "USDT", "LINK"]

# Iterate through the selected tokens
for token in selected_tokens:
    # Check if the token is in the tokens_data dictionary
    if token in tokens_data:
        print(f"Token: {token}")
        print(f"Address: {tokens_data[token]['address']}")
        print(f"Decimals: {tokens_data[token]['decimals']}")
        print(f"LogoURI: {tokens_data[token]['logoURI']}")
        print(f"Name: {tokens_data[token]['name']}")
        print(f"Symbol: {tokens_data[token]['symbol']}")
        print(f"Tags: {tokens_data[token]['tags']}")
        print("\n")
    else:
        print(f"Token {token} not found in the data.\n")

# print (tokens)
# print (tokens[0][0]['symbol'])
# print (tokens[0])
# print (tokens[1])

# print (tokens[token['symbol']])

exit()
CheckBalance (exchange, helper, investment_token)
Check_Allowance (investment_token, 0, exchange, helper, public_key)
swap_result = Swap (exchange, helper, investment_token, token, amount)
# print(swap_result)

GetBalance(exchange, helper, investment_token)
GetBalance(exchange, helper, token)

