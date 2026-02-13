def proof_of_work(block, difficulty=4):
    target = "0" * difficulty

    while True:
        computed_hash = block.compute_hash()
        if computed_hash.startswith(target):
            return computed_hash
        block.nonce += 1
