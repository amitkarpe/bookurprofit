# Sell-token-all.py

from oneinch_py import OneInchSwap, TransactionHelper
import json, csv
from decouple import config
from os import system
import time
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
tokens = json.dumps(tokens, indent=4, sort_keys=True)
json_string = tokens
tokens_data = json.loads(json_string)

# Read the CSV file
selected_tokens = []
with open("list_of_tokens.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip the header

    for row in csv_reader:
        if row:  # Check if the row is not empty
            selected_tokens.append(row[0])
# Iterate through the selected tokens
for token in selected_tokens:
    # Check if the token is in the tokens_data dictionary
    if token in tokens_data:
        print(f"Token: {token}")
        # print(f"Address: {tokens_data[token]['address']}")
        # print(f"Decimals: {tokens_data[token]['decimals']}")
        Check_Allowance (token, 0, exchange, helper, public_key)
        amount = CheckBalance (exchange, helper, token) 
        if amount != 0:
          Swap (exchange, helper, token, "USDC", amount)
          print ("Swap completed successfully ✅✅✅ for token: ", token)
          # GetBalance (exchange, helper, token)
          
        # print(f"Balance: {amount}")
        # result = exchange.get_quote(token, "USDC", amount, decimal=tokens_data[token]['decimals'])
        # print(f"Result: {result}")


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

