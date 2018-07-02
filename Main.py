# Author : xtreme.research@gmail.com
# Requires PyCrypto/PyCryptoDome for Random Number Generator! NOT NECESSARY, just for more secure random numbers and more
# Even Probability Distibution For Better Performance 

from Crypto import Random                         # From Pycryptodome
import hashlib                                    # For SHA256
import time                                       # For Runtime Analysis 
import threading                                  # Miners Run on Several Threads
from Difficulty import System                     # Import basic System Class for checking proof-of-work
from Miner import Miner

Example_System = System()                         # Object to check Proof-Of-Work 256 Bits , intitial Difficulty = 1 
miner_count = 500                                 # Total Number of Miner Threads 
RUNTIME = (120)                                    # For Burnout, Specify time 
start_time = time.time()
miners = []
# Start all miners 

for i in range(miner_count):
    x = Miner(Example_System,i)               
    x.start()    

time.sleep(RUNTIME)
stop_time = time.time()
hashes_count = Example_System.get_total_hashes()
block_count = Example_System.get_block_count()

for miner in miners:
    miner.halt_thread()
# Stats and Math

time_elapsed = stop_time - start_time
hash_rate = (hashes_count/time_elapsed) / 1000
print("-"*60)
print("Total Miner-Threads     : {} ".format(miner_count))
print("Total Blocks Solved     : {} ".format(block_count))
print("Total Hashes Calculated : {} ".format(hashes_count))
print("Total Time Elapsed      : {} Seconds".format(stop_time-start_time))
print("HashRate for the Run    : {} KHashes/Sec".format(hash_rate))
print("-"*60)
