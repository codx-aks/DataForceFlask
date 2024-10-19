from web3 import Web3

ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

if web3.is_connected():
    print("Connected to Ganache")
else:
    print("Failed to connect to Ganache")

contract_address = '0x41AD42731BaF23C663e44ac48757Ee2e2E337e47'
contract_abi = [{
				"anonymous": False,
				"inputs": [
					{
						"indexed": True,
						"internalType": "address",
						"name": "uploader",
						"type": "address"
					},
					{
						"indexed": True,
						"internalType": "address",
						"name": "user",
						"type": "address"
					},
					{
						"indexed": False,
						"internalType": "string",
						"name": "contentHash",
						"type": "string"
					}
				],
				"name": "AccessGranted",
				"type": "event"
			},
			{
				"anonymous": False,
				"inputs": [
					{
						"indexed": True,
						"internalType": "address",
						"name": "uploader",
						"type": "address"
					},
					{
						"indexed": False,
						"internalType": "string",
						"name": "contentHash",
						"type": "string"
					},
					{
						"indexed": False,
						"internalType": "uint256",
						"name": "price",
						"type": "uint256"
					}
				],
				"name": "FileAdded",
				"type": "event"
			},
			{
				"anonymous": False,
				"inputs": [
					{
						"indexed": True,
						"internalType": "address",
						"name": "buyer",
						"type": "address"
					},
					{
						"indexed": False,
						"internalType": "string",
						"name": "contentHash",
						"type": "string"
					}
				],
				"name": "FilePurchased",
				"type": "event"
			},
			{
				"inputs": [
					{
						"internalType": "string",
						"name": "_contentHash",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "_decryptKey",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "_price",
						"type": "uint256"
					}
				],
				"name": "addFile",
				"outputs": [],
				"stateMutability": "nonpayable",
				"type": "function"
			},
			{
				"inputs": [
					{
						"internalType": "uint256",
						"name": "",
						"type": "uint256"
					}
				],
				"name": "allContentHashes",
				"outputs": [
					{
						"internalType": "string",
						"name": "",
						"type": "string"
					}
				],
				"stateMutability": "view",
				"type": "function"
			},
			{
				"inputs": [
					{
						"internalType": "string",
						"name": "_contentHash",
						"type": "string"
					}
				],
				"name": "buyAccess",
				"outputs": [],
				"stateMutability": "payable",
				"type": "function"
			},
			{
				"inputs": [
					{
						"internalType": "string",
						"name": "",
						"type": "string"
					}
				],
				"name": "filesByHash",
				"outputs": [
					{
						"internalType": "string",
						"name": "contentHash",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "decryptKey",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "price",
						"type": "uint256"
					},
					{
						"internalType": "bool",
						"name": "exists",
						"type": "bool"
					},
					{
						"internalType": "address",
						"name": "uploader",
						"type": "address"
					}
				],
				"stateMutability": "view",
				"type": "function"
			},
			{
				"inputs": [
					{
						"internalType": "string",
						"name": "_contentHash",
						"type": "string"
					}
				],
				"name": "getFileData",
				"outputs": [
					{
						"internalType": "string",
						"name": "contentHash",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "decryptKey",
						"type": "string"
					}
				],
				"stateMutability": "view",
				"type": "function"
			},
			{
				"inputs": [],
				"name": "getFiles",
				"outputs": [
					{
						"internalType": "string[]",
						"name": "",
						"type": "string[]"
					}
				],
				"stateMutability": "view",
				"type": "function"
			},
			{
				"inputs": [],
				"name": "getUserFiles",
				"outputs": [
					{
						"components": [
							{
								"internalType": "string",
								"name": "contentHash",
								"type": "string"
							},
							{
								"internalType": "string",
								"name": "decryptKey",
								"type": "string"
							},
							{
								"internalType": "address[]",
								"name": "authorizedUsers",
								"type": "address[]"
							},
							{
								"internalType": "uint256",
								"name": "price",
								"type": "uint256"
							},
							{
								"internalType": "bool",
								"name": "exists",
								"type": "bool"
							},
							{
								"internalType": "address",
								"name": "uploader",
								"type": "address"
							}
						],
						"internalType": "struct FileStorage.File[]",
						"name": "",
						"type": "tuple[]"
					}
				],
				"stateMutability": "view",
				"type": "function"
			},
			{
				"inputs": [
					{
						"internalType": "address",
						"name": "_user",
						"type": "address"
					},
					{
						"internalType": "string",
						"name": "_contentHash",
						"type": "string"
					}
				],
				"name": "grantAccess",
				"outputs": [],
				"stateMutability": "nonpayable",
				"type": "function"
			},
			{
				"inputs": [
					{
						"internalType": "address",
						"name": "",
						"type": "address"
					},
					{
						"internalType": "uint256",
						"name": "",
						"type": "uint256"
					}
				],
				"name": "userFiles",
				"outputs": [
					{
						"internalType": "string",
						"name": "contentHash",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "decryptKey",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "price",
						"type": "uint256"
					},
					{
						"internalType": "bool",
						"name": "exists",
						"type": "bool"
					},
					{
						"internalType": "address",
						"name": "uploader",
						"type": "address"
					}
				],
				"stateMutability": "view",
				"type": "function"
			},
			{
				"inputs": [],
				"name": "withdraw",
				"outputs": [],
				"stateMutability": "nonpayable",
				"type": "function"
			}
		]

private_key="0xa123456789abcdef123456789abcdef123456789abcdef123456789abcdef12"
contract = web3.eth.contract(address=contract_address, abi=contract_abi)
account = "0xd29f37bB5d253B32CA7999F8e2d9166b1F0c8Ca3"
content_hash = "12345"
decrypt_key = "1234"
price = 0

nonce = web3.eth.get_transaction_count(account)

transaction = contract.functions.addFile(content_hash, decrypt_key, price).build_transaction({
    'chainId': 1337,
    'gas': 3000000,
    'gasPrice': web3.to_wei('0', 'gwei'),
    'nonce': nonce
})

balance = web3.eth.get_balance(account)

ether_balance = web3.from_wei(balance, 'ether')
print(f'Account balance: {ether_balance} ETH')
signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)

txn_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)

txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
print(f'Transaction successful with hash: {web3.to_hex(txn_hash)}')
print(f'Transaction receipt: {txn_receipt}')
res = contract.functions.getUserFiles().call()
print(f'test resp: {res}')

