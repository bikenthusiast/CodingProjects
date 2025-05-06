from time import time
import json
from hashlib import sha256

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # scenario 1
        # generate string
        block_string = json.dumps(self.__dict__,sort_keys=True)

        self.hash=sha256(block_string.encode('utf-8')).hexdigest()
        print (self.hash)

        return self.hash

    def __str__(self):
        return (f"Block(index: {self.index}, timestamp: {self.timestamp}, transactions: {self.transactions}, "
                f"previous_hash: {self.previous_hash}, hash: {self.hash})")


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4
        self.pending_transactions = []

    def get_latest_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self):
        # scenario 2
        pass

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    @staticmethod
    def create_genesis_block():
        return Block(0, time(), [], "0")

    @staticmethod
    def is_valid_block(current_block, previous_block):
        if current_block.hash != current_block.calculate_hash():
            raise ValueError(f"Current hash is not valid: {current_block.hash} != {current_block.calculate_hash()}")

        if current_block.previous_hash != previous_block.hash:
            raise ValueError(f"Previous hash is not valid: {current_block.previous_hash} != {previous_block.hash}")

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            try:
                self.is_valid_block(current_block, previous_block)
            except ValueError:
                return False

        return True

    def __str__(self):
        chain_data = ""
        for block in self.chain:
            chain_data += str(block) + "\n"
        return chain_data

index = 1
timestamp = 1620000000.0
transactions = [{"sender": "Alice", "recipient": "Bob", "amount": 50}]
previous_hash = "0" * 64  # 64 zeros for the genesis block
nonce = 0  # Default nonce for mining

# Create the block
block = Block(index, timestamp, transactions, previous_hash, nonce)
print(block)