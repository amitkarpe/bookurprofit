from oneinch_py import OneInchSwap, TransactionHelper, OneInchOracle
import json
from decouple import config
import time

investment_token = "ELK"
# investment_token = "USDC"
# investment_token = "xDAI"
token = "ELK"
token = "USDC"
amount = 0.001
chain = 'gnosis'
public_key = config('public_key')
private_key = config('private_key')
rpc_url = "https://gnosischain-rpc.gateway.pokt.network"


def CheckApproval ():
  get_allowance = exchange.get_allowance(investment_token, public_key)
  # print ("Allowance: ", get_allowance)
  loads = json.loads(json.dumps(get_allowance))
  # print ("Allowance: ", loads.get("allowance"))
  if loads.get("allowance") == '0':
      print ("You need to approve the token first.")
      print ("Approving token: ", investment_token)
      approve_tx = exchange.get_approve(investment_token) # get approval transaction
      built = helper.build_tx(approve_tx) # prepare the transaction for signing, gas price defaults to fast.
      signed = helper.sign_tx(built) # sign the transaction using your private key
      approval_result = helper.broadcast_tx(signed) #broadcast the transaction to the network and wait for the receipt. 
  # else:
  #     print ("Token is approved. ")

def GetBalance ():
  result = helper.get_ERC20_balance(exchange._token_to_address(investment_token))
  if result == 0:
    print ("You don't have any tokens to swap.")
    exit ()
  print ("\n","Token: ", investment_token, "Balance: ", result, "\n")
  return result

exchange = OneInchSwap(public_key, chain=chain) # initialise the OneInchSwap object as "exchange"
helper = TransactionHelper(rpc_url, public_key, private_key, chain=chain) # initialise the TransactionHelper object as "helper"
oracle = OneInchOracle(rpc_url, chain=chain) # initialise the OneInchOracle object as "oracle"
print ("\n","Token: ", token, "Balance: ", helper.get_ERC20_balance(exchange._token_to_address(token),decimal=6), "\n")
result = GetBalance ()
# amount = GetBalance ()

token = "GNO"
token =  "WETH"
# token = "BUSD"
investment_token =  "BUSD"
investment_token =  "USDC"
# rate = oracle.get_rate(src_token=exchange._token_to_address(token), dst_token=exchange._token_to_address(investment_token), src_token_decimal=18, dst_token_decimal=6)

token = "ELK"
token = "GNO"
investment_token = "WXDAI"
rate = oracle.get_rate(src_token=exchange._token_to_address(token), dst_token=exchange._token_to_address(investment_token), src_token_decimal=18, dst_token_decimal=18)
print ("1 ", token,"= ", rate, investment_token)
# def get_rate(self, src_token, dst_token, wrap=False, src_token_decimal: int = 18, dst_token_decimal: int = 18):

# exit ()

CheckApproval ()

swap_tx = exchange.get_swap(investment_token, token, amount, 2) # get the swap transaction
result = helper.build_tx(swap_tx) # prepare the transaction for signing, gas price defaults to fast.
result = helper.sign_tx(result) # sign the transaction using your private key
swap_result = helper.broadcast_tx(result) #broadcast the transaction to the network and wait for the receipt. 

print ("\n","Token: ", token, "Balance: ", helper.get_ERC20_balance(exchange._token_to_address(token),decimal=6), "\n")
print ("\n","Token: ", investment_token, "Balance: ", helper.get_ERC20_balance(exchange._token_to_address(investment_token)), "\n")

# print(swap_result)