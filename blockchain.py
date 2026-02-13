from block import Block
from pow import proof_of_work

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block(0, "Genesis Block", "0")
        genesis.hash = proof_of_work(genesis, self.difficulty)
        self.chain.append(genesis)

    def add_block(self, data):
        last_block = self.chain[-1]
        new_block = Block(last_block.index + 1, data, last_block.hash)
        new_block.hash = proof_of_work(new_block, self.difficulty)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.previous_hash != previous.hash:
                return False

            if current.compute_hash() != current.hash:
                return False

        return True
