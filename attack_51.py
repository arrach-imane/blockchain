from blockchain import Blockchain

# Nœuds honnêtes
node1 = Blockchain(difficulty=4)
node2 = Blockchain(difficulty=4)

# Attaquant (plus puissant)
attacker = Blockchain(difficulty=2)

#  MINAGE HONNÊTE
node1.add_block("Imane -> Salma : 10")
node1.add_block("Salma-> Hind : 5")

node2.add_block("Imane-> Salma : 10")
node2.add_block("Salma-> Hind : 5")

# Copie de la chaine par l'attaquantS
attacker.chain = node1.chain[:]

# CRÉATION D’UNE CHAÎNE MALVEILLANTE
attacker.add_block("Imane -> Salma: 1000 (FAKE)")

# COURSE À LA CHAÎNE LA PLUS LONGUE
while len(attacker.chain) <= len(node1.chain):
    attacker.add_block("Attacker extra block")
    
# CONSENSUS
chains = [node1, node2, attacker]

winner = max(chains, key=lambda bc: len(bc.chain))

if winner == attacker:
    print(" Attaque 51% réussie")
else:
    print("Réseau honnête résistant")
# AFFICHAGE DES BLOCKCHAINS

def display_chain(blockchain, name):
    print(f"\n📦 Blockchain de {name}")
    print("=" * 60)
    for block in blockchain.chain:
        print(f"Index        : {block.index}")
        print(f"Timestamp    : {block.timestamp}")
        print(f"Data         : {block.data}")
        print(f"Nonce        : {block.nonce}")
        print(f"Prev Hash    : {block.previous_hash}")
        print(f"Hash         : {block.hash}")
        print("-" * 60)

# APPELS D’AFFICHAGE (EN DEHORS)

display_chain(node1, "Nœud honnête 1")
display_chain(node2, "Nœud honnête 2")
display_chain(attacker, "Attaquant")
