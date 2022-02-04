# Module 1 - Create Blockchain


import datetime
import haslib
import json
from flask import Flas, jsonify

# Part 1 - Building a Blockchain

class Blockchain:
  
    def __init__(self):
        self.chain = [] #list containing the diff blocks
        self.create_block(proof = 1, previous_hash = '0') #genesis block
        
    def create_block(self, proof, previous_hash) : 
        block = {'index' :len(self.chain) + 1, 
                 'timestamp' : str(datetime.datetime.now()),
                 'proof' : proof,
                 'previous_hash' : previous_hash}
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof) :
        check_proof = False # once we find the proof that's the solution of the problem this will change to true
        new_proof = 1 #to solve the problem we are going to increent the new_proof at each iteration until we've the right proof
        while check_proof is False:
            #miners problem. The more leading zeros the longer the problem
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000'
                check_proof = True
            else: 
                new_proof +=1
        return new_proof
    
    def hash(self, block) :  #take a block as input and will return the sha of the block
           encoded_block = json.dumps(block, sort_keys = True).encode()
           return hashlib.sha256(encoded_block).hexdigest()
       
    def is_chain_valid(self, chain) :
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previos_hash'] != self.hash(previos_block):
                return False
            else:
                previous_proof = previous_block['proof']
                proof = block['proof']
                hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
        

# Part 2 - Mining our Blockchain