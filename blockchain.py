import hashlib
import time
from collections import defaultdict

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash, miner):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
    
        self.previous_hash = previous_hash
        self.miner = miner
        self.nonce = 0
        self.hash = self.mine_block()

    def calculate_hash(self):
        block_data = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.nonce}{self.miner}"
        return hashlib.sha256(block_data.encode()).hexdigest()

    def mine_block(self, difficulty=4):
        target = "0" * difficulty
        while True:
            hash_attempt = self.calculate_hash()
            if hash_attempt.startswith(target):
                return hash_attempt
            self.nonce += 1

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4
        self.reward = 3
        self.pending_transactions = []

    def create_genesis_block(self):
        return Block(0, time.time(), [{"from": "Sistem", "to": "Genesis", "amount": 0}], "0", "Sistem")

    def get_latest_block(self):
        return self.chain[-1]

    def create_transaction(self, sender, receiver, amount):
        self.pending_transactions.append({"from": sender, "to": receiver, "amount": amount})

    def mine_pending_transactions(self, miner_name):
      
        reward_tx = {"from": "Sistem", "to": miner_name, "amount": self.reward}
        transactions = [reward_tx] + self.pending_transactions
        block = Block(len(self.chain), time.time(), transactions, self.get_latest_block().hash, miner_name)
        self.chain.append(block)
        self.pending_transactions = []
        print(f"{miner_name} berhasil mining block #{block.index} dan mendapat {self.reward} koin!")

    def get_balance(self, name):
        balance = 0
        for block in self.chain:
            for tx in block.transactions:
                if tx["from"] == name:
                    balance -= tx["amount"]
                if tx["to"] == name:
                    balance += tx["amount"]
        return balance

    def print_balances(self):
        balances = defaultdict(int)
        for block in self.chain:
            for tx in block.transactions:
                balances[tx["from"]] -= tx["amount"]
                balances[tx["to"]] += tx["amount"]
        print("\nSaldo semua pengguna:")
        for user, amount in balances.items():
            print(f"{user}: {amount} koin")

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

bc = Blockchain()

for miner in ["Abim", "Reoy", "Panji", "Ucok", "Patih"]:
    bc.mine_pending_transactions(miner)

for name in ["Abim", "Reoy", "Panji", "Ucok", "Patih"]:
    bc.create_transaction("Lintar", name, 2)

bc.mine_pending_transactions("Reoy")

print("\n=== RANTAI BLOK ===")
for block in bc.chain:
    print(f"\nBlock #{block.index} oleh {block.miner}")
    print(f"Hash: {block.hash}")
    print(f"Previous: {block.previous_hash}")
    print("Transaksi:")
    for tx in block.transactions:
        print(f"- {tx['from']} kirim {tx['amount']} koin ke {tx['to']}")


bc.print_balances()

print("\nBlockchain valid:", bc.is_chain_valid())
