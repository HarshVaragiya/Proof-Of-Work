# Author : xtreme.research@gmail.com
# Requires PyCrypto/PyCryptoDome for Random Number Generator! NOT NECESSARY, just for more secure random numbers and more
# Even Probability Distibution For Better Performance 

from Crypto import Random                         # From Pycryptodome
import hashlib                                    # For SHA256
import time                                       # For Runtime Analysis 
import threading                                  # Miners Run on Several Threads
from Difficulty import System                     # Import basic System Class for checking proof-of-work

a = System(256,1)                                 # Object to check Proof-Of-Work 256 Bits , intitial Difficulty = 1 
miner_count = 500                                 # Total Number of Miner Threads 
block_count = 0                                   # Total Blocks Counted  
hashes_count = 0                                  # Total Hashes Calculated
runtime = 120                                     # For Burnout, Specify time 

start_time = time.time()                          # Log start time 
last_time = start_time                            # time when last block was solved

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
        global hashes_count,last_time
        while self.stay_alive == True:
            time.sleep(self.time_delay)         # To demonstrate slower hash rates
            self.h = self.generate_hash()
            hashes_count +=1
            if(self.System_Obj.check_hash(self.h) == True):        # if block is solved 
                global block_count
                block_count +=1
                print("Block {} Solved By Miner Thread : {} ".format(block_count,self.thread_id))
                print("Time to Solve BLock             : {} ".format(time.time()-last_time))
                last_time = time.time()
                print("Difficulty                      : {} ".format(2**self.System_Obj.show_difficulty()))
            else:
                #print(self.h)
                pass

    def halt_thread(self):
        self.stay_alive = False

miners = []

# Start all miners 
for i in range(miner_count):
    x = Miner(a,i)               
    x.start()                       

time.sleep(runtime)

for miner in miners:
    miner.halt_thread()

stop_time = time.time()

# Stats and Math 

time_elapsed = stop_time - start_time
hash_rate = (hashes_count/time_elapsed) / 1000

print("-"*60)
print("Total Miner-Threads     : {} ".format(miner_count))
print("Total Blocks Solved     : {} ".format(block_count))
print("Total Hashes Calculated : {} ".format(hashes_count))
print("Total Time Elapsed      : {} Seconds".format(time_elapsed))
print("HashRate for the Run    : {} KHashes/Sec".format(hash_rate))
print("-"*60)
