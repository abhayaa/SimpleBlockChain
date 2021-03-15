import hashlib
import time


class Block: 
    
    def __init__(self, index, proof_no, prev_hash, transactions, timestamp=None):
        self.index = index
        self.proof_no = proof_no
        self.prev_hash = prev_hash
        self.transactions = transactions
        self.timestamp = timestamp or time.time()

    @property
    def calculate_hash(self):
        string_to_hash = "{}{}{}{}{}".format(self.index, self.proof_no,
                                             self.prev_hash, self.transactions,
                                             self.timestamp)

        return hashlib.sha256(string_to_hash.encode()).hexdigest()

    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.index, self.proof_no,
                                               self.prev_hash, self.transactions,
                                               self.timestamp)



