import sys
sys.path.append('/Users/renegadeconfidence/workspace/bitcoin')

from blockchain.backend.core.block import Block
from blockchain.backend.core.blockheader import BlockHeader
from blockchain.backend.util.util import hash256
import time

ZERO_HASH = '0' * 64
VERSION = 1

class Blockchain:
    def __init__(self):
        self.chain = []
        self.GenesisBlock()
    
    def GenesisBlock(self):
        BlockHeight = 0
        prevBlockHash = ZERO_HASH
        self.addBlock(BlockHeight, prevBlockHash)

    def addBlock(self, BlockHeight, prevBlockHash):
        timestamp = int(time.time())
        Transaction = f"AfriCoiner Alert sent {BlockHeight} Bitcoins to Renegade"
        merkleRoot = hash256(Transaction.encode()).hex()
        bits = 'ffff001f'
        blockheader = BlockHeader(VERSION, prevBlockHash, merkleRoot, timestamp, bits)
        blockheader.mine()
        self.chain.append(Block(BlockHeight, 1, blockheader, 1, Transaction))

if __name__ == "__main__":
    blockchain = Blockchain()



