import json
from web3 import Web3
from flask import Flask, jsonify
from flask_cors import CORS
from web3.middleware import geth_poa_middleware


def get_transaction_data(transaction_hash):

    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/8365b38a49eb4cb899edfe72b3ddc252'))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    Transaction_data = w3.eth.get_transaction(transaction_hash)  
    print(Transaction_data)

transaction_hash =  input("Enter Transaction Hash: ")
get_transaction_data((transaction_hash))
