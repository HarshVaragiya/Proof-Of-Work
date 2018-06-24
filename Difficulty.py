# Author : xtreme.research@gmail.com
# Class Definition of CryptoSystem which checks for given hash for proof-of-work

# Basic Function that Exponentially Increases the difficulty, so Time to Solve increases Exponentially 
def Exponential(init_bit_length):
    return init_bit_length+1

class System:
    
    def __init__(self,BIT_LEN=256,INITIAL_TARGET_BITS=1,DIFFICULTY_UPDATE_FUNCTION=Exponential):     # Init 
        self.bit_len = BIT_LEN                                                 # SHA256 so 256 bits
        self.bit_modifier = INITIAL_TARGET_BITS                                # Staring difficulty 
        self.update_func = DIFFICULTY_UPDATE_FUNCTION                          # When Block is Solved, Update Target
        self.calc_target()                                                     # Calculate Target Value 
    
    def calc_target(self):
        self.target = (2**(self.bit_len-self.bit_modifier))                    # 2 ^ (256-difficulty) so smaller values for 
                                                                               # greater difficulty
    def show_difficulty(self):                                                 
        return self.bit_modifier                                               # show difficulty in bits
    
    def on_solve(self):                                                        # when block is solved, update
        self.bit_modifier = self.update_func(self.bit_modifier)                # and calculate target again
        self.calc_target()

    def check_hash(self,chk_hash):                                             # basic function to check given hash
        if chk_hash<self.target:                                               # against target value 
            self.on_solve()
            return True
        else:
            return False
