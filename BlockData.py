from web3 import Web3
from web3.middleware import geth_poa_middleware


w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/8365b38a49eb4cb899edfe72b3ddc252'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
print(w3)
print(w3.isConnected())

block_number = w3.eth.blockNumber

Block_data = w3.eth.get_block(block_number)
print("Block Number: ", block_number)
print(Block_data)
print("Block Hash: ", Block_data['hash'])
print("Block Timestamp: ", Block_data['timestamp'])
print("Block Transactions: ", Block_data['transactions'])
