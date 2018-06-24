def Exponential(init_bit_length):
    return init_bit_length+1

class System:
    
    def __init__(self,BIT_LEN=256,INITIAL_TARGET_BITS=1,DIFFICULTY_UPDATE_FUNCTION=Exponential):
        self.bit_len = BIT_LEN
        self.bit_modifier = INITIAL_TARGET_BITS
        self.update_func = DIFFICULTY_UPDATE_FUNCTION
        self.calc_target()
    
    def calc_target(self):
        self.target = (2**(256-self.bit_modifier)) 

    def show_difficulty(self):
        return self.bit_modifier
    
    def on_solve(self):
        self.bit_modifier = self.update_func(self.bit_modifier)
        self.calc_target()

    def check_hash(self,chk_hash):
        if chk_hash<self.target:
            self.on_solve()
            return True
        else:
            return False