from blocks import Block
blockchain = []
genesis_block = Block("Chancellor on tea brink",["Satoshi sent 1 BTC to Me","Whats Up Doc"])
second_block = Block(genesis_block.block_hash,["Hiiiiiiii","Goooooddd"])
third_block = Block(second_block.block_hash,["WWWAWfaafa","gagagagdjdf"])
print(genesis_block.block_hash)
print(second_block.block_hash)
print(third_block.block_hash)
