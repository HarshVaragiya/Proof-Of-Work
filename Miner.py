# Author : xtreme.research@gmail.com
# Class Definition for miner of the current system.
# Requires PyCrypto/PyCryptoDome for Random Number Generator! NOT NECESSARY, just for more secure random numbers and more
# Even Probability Distibution For Better Performance 

from Crypto import Random                         # From Pycryptodome
import hashlib                                    # For SHA256
import time                                       # For Runtime Analysis 
import threading                                  # Miners Run on Several Threads
from Difficulty import System                     # Import basic System Class for checking proof-of-work

class Miner(threading.Thread):                    # Threaded
    def __init__(self,SYSTEM_TARGET_OBJECT,thread_id=0,timer_delay=0.0,random_byte_length=256):
        threading.Thread.__init__(self)          
        self.thread_id = thread_id                # Thread ID
        self.daemon = True                        # So threads exit when program exits 
        self.time_delay = timer_delay             # Time Delay to demonstrate lower hash rates
        self.random_byte_length = random_byte_length # random byte length for pycryptodome random bytes generator
        self.System_Obj = SYSTEM_TARGET_OBJECT    # Object to check proof of work 
        self.stay_alive = True                    # Thread Killing Thingy
    
    def get_random_int(self,bytess):              # Change Random Function if required
        return Random.get_random_bytes(bytess)    # this is cryptographically Secure so better probability distibution
    
    def generate_hash(self):                      # get int of the hash of the random number 
        self.x = self.get_random_int(self.random_byte_length)
        self.hash = hashlib.sha256(self.x).hexdigest()
        self.ret = int(self.hash,16)
        time.sleep(self.time_delay)
        return self.ret
    
    def run(self):
        while self.stay_alive == True:
            time.sleep(self.time_delay)                            # To demonstrate slower hash rates
            self.h = self.generate_hash()
            if(self.System_Obj.check_hash(self.h) == True):        # if block is solved 
                #print("Hash {} - By Miner Thread {}".format(self.h,self.thread_id))
                pass
            else:
                #print(self.h)
                pass

    def halt_thread(self):
        self.stay_alive = False
        self.is_alive = False

#End of class definition
