# intial_setup.py

from oneinch_py import OneInchSwap, TransactionHelper
import json

def Swap (exchange, helper, investment_token, token, amount):
    # print("amount:", amount)
    # print(type (amount))
    swap_tx = exchange.get_swap(investment_token, token, amount , 5) # get the swap transaction
    # print("Swap Transaction:", swap_tx)
    # print("Swap amount:", swap_tx['fromTokenAmount'])
    # print(type (swap_tx['fromTokenAmount']))
    # print("Swap Transaction:", swap_tx['tx'])
    # print("Swap Transaction - gasPrice:", swap_tx['tx']['gasPrice'])
    # print("Swap Transaction - gas:", swap_tx['tx']['gas'])
    # swap_tx['gasPrice'] = int (int (swap_tx['gasPrice']) * 1.5)
    # swap_tx['tx']['gas'] = 70000
    result = helper.build_tx(swap_tx) # prepare the transaction for signing, gas price defaults to fast.
    result = helper.sign_tx(result) # sign the transaction using your private key
    swap_result = helper.broadcast_tx(result) #broadcast the transaction to the network and wait for the receipt. 
    print("")
    return swap_result
