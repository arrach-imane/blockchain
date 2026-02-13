from blockchain import Blockchain
import time
bc_easy = Blockchain(difficulty=1)

bc_easy.add_block("Tx 1")
bc_easy.add_block("Tx 2")

bc_hard = Blockchain(difficulty=4)

bc_hard.add_block("Tx 1")
bc_hard.add_block("Tx 2")


start = time.time()
bc_easy.add_block("Attack")
print("Temps difficulté faible :", time.time() - start)

start = time.time()
bc_hard.add_block("Attack")
print("Temps difficulté élevée :", time.time() - start)
