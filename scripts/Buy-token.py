# Buy-token.py

from oneinch_py import OneInchSwap, TransactionHelper
import json
from decouple import config
from os import system
import sys
from intial_setup import setup_rpc_url, Exiting, Check_Allowance, CheckBalance, GetBalance
from swap import Swap
from decimal import Decimal, ROUND_DOWN

# pip install python-decouple 1inch.py==1.8.2 requests==2.28.1 web3<6.0
public_key = config('public_key')
private_key = config('private_key')


if len(sys.argv) != 5:
    print("Usage: python Buy-token.py <blockchain> <investment token> <buy token> <buying amount with decimal>")
    print("Example: python Buy-token.py polygon USDC QUICK 0.0001")
    sys.exit(1)


chain = sys.argv[1]
rpc_url = setup_rpc_url(chain)
print ("Chain:", chain)
print ("RPC URL:", rpc_url)
print ("Public Key:", public_key)
investment_token = sys.argv[2]
token = sys.argv[3]
amount = float(sys.argv[4])

print("Investment Token:", investment_token)
print("Buy Token:", token)
print("Buying Amount:", amount)

exchange = OneInchSwap(public_key, chain=chain) # initialise the OneInchSwap object as "exchange"
helper = TransactionHelper(rpc_url, public_key, private_key, chain=chain) # initialise the TransactionHelper object as "helper"
CheckBalance (exchange, helper, investment_token)
Check_Allowance (investment_token, 0, exchange, helper, public_key)
swap_result = Swap (exchange, helper, investment_token, token, amount)
# print(swap_result)

GetBalance(exchange, helper, investment_token)
GetBalance(exchange, helper, token)
