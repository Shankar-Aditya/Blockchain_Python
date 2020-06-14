#libraries needed
import web3
from web3 import Web3
ganache_url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())

#Ganache addresses and private key of one of these address
account_1 = "##########################################"
account_2 = "******************************************"
private_key = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
#get nonce-prevents two or more transcations
nonce = web3.eth.getTransactionCount(account_1)
#Building transaction btw accounts
tx = {'nonce': nonce,
     'to': account_2,
     'value': web3.toWei(1, 'ether'),
     'gas': 2000000,
     'gasPrice': web3.toWei('50', 'gwei')
     }

#Sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)
#Send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
#Get transaction hash
print(web3.toHex(tx_hash))

