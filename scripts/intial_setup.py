# intial_setup.py

from oneinch_py import OneInchSwap, TransactionHelper
import json, time


def CheckBalance (exchange, helper, investment_token, decimal_places):
  # print("decimal_places: ", decimal_places)
  balance = helper.get_ERC20_balance(exchange._token_to_address(investment_token), decimal=decimal_places)
  small_number=0.0000000000000001
  small_number = 0.00000000000001
  small_number = 0.0000000000001
#   print("small_number: ", small_number)
  # Check if the balance is greater than 0 and greater than small_number (0.00000000000000001) to avoid rounding errors ( avoid dust amounts)
  if balance > 0 and balance > small_number:
    if investment_token == "USDC" or investment_token == "USDT":
        decimal_places = 6
        # print("decimal_places: ", decimal_places)
        print ("\n","Token: ", investment_token, "Balance: ", format(balance, f".{decimal_places}f"), "i.e.", balance)
  else:
    print ("You don't have any tokens to swap. 😭😭😭😭😭")
    print ("\n","Token: ", investment_token, "Balance: ", format(balance, f".{decimal_places}f"), "i.e.", balance, "\n")
    return 0
  return balance

def GetBalance (exchange, helper, investment_token, decimal_places):
  if investment_token == "USDC" or investment_token == "USDT":
    decimal_places = 6
  print("decimal_places: ", decimal_places)
  balance = helper.get_ERC20_balance(exchange._token_to_address(investment_token), decimal=decimal_places)
  # print ("Token: ", investment_token, "Balance: ", format(balance, f".{decimal_places}f"), "i.e.", balance, "\n")
  print ("Token: ", investment_token, "Balance: ", format(balance, f".{decimal_places}f"))
  return balance


# https://app.infura.io/dashboard/ethereum/d162e1d2d54e4fd5b07a78b9b9176728/settings/endpoints

# https://github.com/RichardAtCT/1inch_wrapper/blob/f515f0dc807d0654edfc845b4ef265b8b6ae2d97/oneinch_py/main.py#L325
# class OneInchOracle:
#     chains = {
#         "ethereum": '1',
#         "binance": '56',
#         "polygon": "137",
#         "optimism": "10",
#         "arbitrum": "42161",
#         "gnosis": "100",
#         "avalanche": "43114",
#         "fantom": "250"
#     }

# Write a function to setup RPC URL based on the chain
def setup_rpc_url(chain):
    if chain == "polygon":
        rpc_url = "https://polygon-mainnet.infura.io/v3/d162e1d2d54e4fd5b07a78b9b9176728"
    elif chain == "binance":
        rpc_url = "https://bsc-dataseed.binance.org/"
    elif chain == "ethereum":
        rpc_url = "https://mainnet.infura.io/v3/d162e1d2d54e4fd5b07a78b9b9176728"
    elif chain == "arbitrum":
        rpc_url = "https://arbitrum-mainnet.infura.io/v3/d162e1d2d54e4fd5b07a78b9b9176728"
    elif chain == "optimism":
        rpc_url = "https://optimism-mainnet.infura.io/v3/d162e1d2d54e4fd5b07a78b9b9176728"
    elif chain == "avalanche":
        rpc_url = "https://avalanche-mainnet.infura.io/v3/d162e1d2d54e4fd5b07a78b9b9176728"
    # https://chainlist.org/chain/250
    elif chain == "fantom":
        rpc_url = "https://fantom-mainnet.gateway.pokt.network/v1/lb/62759259ea1b320039c9e7ac"
    # https://chainlist.org/chain/100
    elif chain == "gnosis":
        rpc_url = "https://gnosischain-rpc.gateway.pokt.network"
    return rpc_url


def Exiting(statusCode):
    statusCode = statusCode
    print ("Exiting")
    return {
      "isBase64Encoded": "false",
      "statusCode": statusCode,
      "body": '{"message": "successful"}',
      # "body": final_body,
      "headers": {
          "content-type": "application/json"
      }
    }
    # logger.info('Total Errors: {}'.format("Exiting"))
    # sys.exit(0)

def Check_Allowance (investment_token, amount, exchange, helper, public_key):
    get_allowance = exchange.get_allowance(investment_token, public_key)
    # print ("Allowance: ", get_allowance)
    loads = json.loads(json.dumps(get_allowance))
    # print ("Allowance: ", loads.get("allowance"))
    # print (type(loads.get("allowance")))
    # print ("Amount: ", amount)
    # compare allowance with amount as long interger and approve if allowance is less than amount
    # convert allowance to long interger
    allowance = int(loads.get("allowance"))
    # print ("Allowance: ", allowance)
    # print (type(allowance))
    
    # if loads.get("allowance") == '0':
    if allowance <= 0 :
        print ("You need to approve the token first.")
        print ("Approving token: ", investment_token)
        approve_tx = exchange.get_approve(investment_token) # get approval transaction
        # print ("approve_tx: ", approve_tx)
        # approve_tx['gasPrice'] = int (approve_tx['gasPrice'] )
        # approve_tx['gasPrice'] = int (int (approve_tx['gasPrice']) * 1.5)
        # print ("approve_tx: ", approve_tx)
        # approve_tx['gas'] = 70000
        built = helper.build_tx(approve_tx,  speed='high') # prepare the transaction for signing, gas price defaults to fast.
        signed = helper.sign_tx(built) # sign the transaction using your private key
        approval_result = helper.broadcast_tx(signed) #broadcast the transaction to the network and wait for the receipt. 
        time.sleep(5)
        return approval_result
    else:
        # print ("You have allowance ✅.\n")
        print("")