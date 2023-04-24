# intial_setup.py

from oneinch_py import OneInchSwap, TransactionHelper
import json

def Swap (exchange, helper, investment_token, token, amount):

    swap_tx = exchange.get_swap(investment_token, token, amount , 5) # get the swap transaction
    result = helper.build_tx(swap_tx) # prepare the transaction for signing, gas price defaults to fast.
    result = helper.sign_tx(result) # sign the transaction using your private key
    swap_result = helper.broadcast_tx(result) #broadcast the transaction to the network and wait for the receipt. 
    return swap_result
