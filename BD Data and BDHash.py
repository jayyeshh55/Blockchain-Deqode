import json
from web3 import Web3
from flask import Flask, jsonify
from flask_cors import CORS
from web3.middleware import geth_poa_middleware



def get_block_data_num(block_number):
    
    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/8365b38a49eb4cb899edfe72b3ddc252'))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    Block_data_using_num = w3.eth.get_block(block_number)  
    print(Block_data_using_num)

block_number = int(input("Enter Block Number: "))
get_block_data_num(block_number)

print("\n")

def get_block_data_hash(block_hash):
   w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/8365b38a49eb4cb899edfe72b3ddc252'))
   w3.middleware_onion.inject(geth_poa_middleware, layer=0)

   
   Block_data_using_hash = w3.eth.get_block(block_hash)  
   print(Block_data_using_hash)

block_hash = input("Enter Block Hash: ")
get_block_data_hash(block_hash)

print("\n")


