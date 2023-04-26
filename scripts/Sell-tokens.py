# Sell-tokens.py
# Sell Tokens by passing a comma-separated list of tokens as a command-line argument.
# python Sell-tokens.py gnosis "WETH, USDT, LINK" 10
from oneinch_py import OneInchSwap, TransactionHelper
import json, sys, time
from decouple import config
from intial_setup import setup_rpc_url, Exiting, Check_Allowance, CheckBalance, GetBalance
from swap import Swap
from decimal import Decimal, ROUND_DOWN

public_key = config('public_key')
private_key = config('private_key')
investment_token = "USDC"

if len(sys.argv) <= 2:
    print("Usage: python Sell-token-all.py <blockchain> <tokens>")
    print("Example: python Sell-token-all.py polygon \"ETH, USDT, LINK, UNI\"")
    sys.exit(1)

chain = sys.argv[1]
rpc_url = setup_rpc_url(chain)
percentage = sys.argv[3]

exchange = OneInchSwap(public_key, chain=chain) # initialise the OneInchSwap object as "exchange"
helper = TransactionHelper(rpc_url, public_key, private_key, chain=chain) # initialise the TransactionHelper object as "helper"

tokens_data = exchange.get_tokens()

# Get the selected tokens from the command line argument
selected_tokens = sys.argv[2].split(', ')

# Iterate through the selected tokens
for token in selected_tokens:
    # Check if the token is in the tokens_data dictionary
    if token in tokens_data:
        print(f"Token: {token}")
        decimal_places = tokens_data[token]['decimals']
        print(f"Decimals: {tokens_data[token]['decimals']}")
        amount = CheckBalance (exchange, helper, token, decimal_places) 
        if amount != 0:
            Check_Allowance(token, 0, exchange, helper, public_key)
            final_amount = Decimal(amount) * (Decimal(percentage) / Decimal(100))
            # Round the final_amount to the appropriate number of decimal places
            rounded_final_amount = final_amount.quantize(Decimal(10) ** -decimal_places, rounding=ROUND_DOWN)
            # Format the rounded balance as a string
            formatted_final_amount = float (format(rounded_final_amount, f".{decimal_places}f"))
            # print(f"Final amount = {format(amount, f'.{decimal_places}f')} X {percentage} / 100 ==> {format(formatted_final_amount, f'.{decimal_places}f')}")
            print(f"Final amount: ({percentage} % of {format(amount, f'.{6}f')}) ==> {format(formatted_final_amount, f'.{6}f')}")
            amount = formatted_final_amount
            # Pass the rounded_final_amount (as Decimal) to the Swap function
            Swap(exchange, helper, token, investment_token, amount)
            print(f"Swaped {token} completed successfully ✅ for token: {investment_token}\n")

        # print("\n")
    else:
        print(f"Token {token} not found in the data.\n")

print("\nCompleted successfully ✅✅✅")
exit()
