from blockchain import Blockchain

bc = Blockchain(difficulty=4)

bc.add_block("Alice -> Bob : 50")
bc.add_block("Bob -> Charlie : 25")

print("Blockchain valide ?", bc.is_valid())

for block in bc.chain:
    print("-" * 60)
    print("Index:", block.index)
    print("Nonce:", block.nonce)
    print("Hash:", block.hash)
    print("Previous:", block.previous_hash)
    print("Data:", block.data)
bc.chain[1].data = "Alice -> Bob : 5000"
print(bc.is_valid())
for block in bc.chain:
    print("-" * 60)
    print("Index:", block.index)
    print("Nonce:", block.nonce)
    print("Hash:", block.hash)
    print("Previous:", block.previous_hash)
    print("Data:", block.data)
