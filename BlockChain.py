from Block import Block
import hashlib

class BlockChain:

    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()
        self.construct_genesis()

    def construct_genesis(self):
        self.construct_block(proof_no = 0, prev_hash = 0)

    def construct_block(self, proof_no, prev_hash):
        block = Block(
            index  = len(self.chain),
            proof_no = proof_no,
            prev_hash = prev_hash,
            transactions = self.current_transactions)

        self.current_transactions = []

        self.chain.append(block)

        return block

    @staticmethod
    def check_validity():
        if prev_block.index + 1 != block.index:
            return False

        elif prev_block.calcuate_hash != block.prev_hash:
            return False

        elif not BlockChain.verifying_proof(block.proof_no, prev_block, proof_no):
            return False
        
        elif block.timestamp <= prev_block.timestamp:
            return False

    def new_data(self, sender, recipient, quantity):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'quantity': quantity
        })

        return True

    @staticmethod
    def proof_of_work(last_proof):
        proof_no = 0
        while BlockChain.verifying_proof(proof_no, last_proof) is False:
            proof_no +=1

        return proof_no

    @staticmethod
    def verifying_proof(last_proof, proof):
        guess = f'{last_proof, proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @property
    def last_block(self):
        return self.chain[-1]


    def block_minin(self, details_miner):

        self.new_data(
            sender = "0",
            receiver = details_miner,
            quantity = 1
        )

        last_block = self.latest_block


        last_proof_no = last_block.last_proof_no
        proof_no = self.proof_of_work(last_proof_no)

        last_hash = last_block.calculate_hash
        block = self.construct_block(proof_no, last_hash)

        return vars(block)


    def create_node(self, address):
        self.nodes.add(address)
        return True


    @staticmethod
    def obtain_block_object(block_data):

        return Block(
            block_data['index'],
            block_data['proof_no'],
            block_data['prev_hash'],
            block_data['data'],
            timestamp=block_data['timestamp'])
        