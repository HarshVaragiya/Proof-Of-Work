# Author : xtreme.research@gmail.com
# Class Definition of CryptoSystem which checks for given hash for proof-of-work

# Basic Function that Exponentially Increases the difficulty, so Time to Solve increases Exponentially 

import time                                                            # Calculate Time Elapsed Per Block and stuff

blocks_solved = 0                                                      # Total Blocks Solved
hashes_count  = 0                                                      # Total Hashes Checked

def Exponential(bit_length):               # Exponentially increasing Time Complexity O(2ⁿ)
    target = (2**256)/(2**(bit_length+1))
    return target

def Linear(bit_len):                       # Linearly increasing Time Complexity O(n)
    global blocks_solved
    return ((2**256)/blocks_solved)

def Set_Arbitary_Difficulty_With_Inverse_Probability(one_by_probability): # Set Arbitary Difficulty - Time Complexity O(n)
    return ((2**256)/one_by_probability)

class System:

    def __init__(self,BIT_LEN=256,INITIAL_TARGET_BITS=1,DIFFICULTY_UPDATE_FUNCTION=Exponential):     # Init 
        self.bit_len = BIT_LEN                                                 # SHA256 so 256 bits
        self.bit_modifier = INITIAL_TARGET_BITS                                # Staring difficulty 
        self.update_func = DIFFICULTY_UPDATE_FUNCTION                          # When Block is Solved, Update Target
        self.update_difficulty()                                               # Calculate Target Value 
        self.start_time = time.time()
        self.last_solve_time = time.time()
    
    def get_difficulty(self):
        p = (2**self.bit_len)/self.target
        return p
    
    def update_difficulty(self):
        self.target = self.update_func(self.bit_modifier)

    def on_solve(self,hash_block):
        global blocks_solved,hashes_count                                      # when block is solved, update
        self.solve_time = time.time() - self.last_solve_time
        self.last_solve_time = time.time()
        blocks_solved +=1
        self.update_difficulty()
        self.bit_modifier+=1

        #print("-"*60)
        #print("Block Solved  : {} \nTime To Solve : {} \nTotal Hashes : {}".format(blocks_solved,self.solve_time,hashes_count))
        print()
        print("Block  Solved  : {} ".format(blocks_solved) )
        print("Time to Solve  : {} ".format(self.solve_time))
        print("Total Hashes   : {} ".format(hashes_count))
        print("Hash of Block  : {} ".format(hash_block))
        print("New Difficulty : {} ".format(self.get_difficulty()))


    def check_hash(self,chk_hash):                                             # basic function to check given hash
        global hashes_count
        hashes_count +=1
        #print(chk_hash)
        if chk_hash<self.target:                                               # against target value 
            self.on_solve(chk_hash)
            return True
        else:
            return False
    
    def get_total_hashes(self):
        global hashes_count
        return hashes_count
    
    def get_block_count(self):
        global blocks_solved
        return blocks_solved
