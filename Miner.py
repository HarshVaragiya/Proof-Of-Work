from Crypto import Random
import hashlib
import time
import threading
from Difficulty import System

a = System(256,1)
miner_count = 500
block_count = 0
hashes_count = 0
runtime = 120

start_time = time.time()
last_time = start_time

class Miner(threading.Thread):
    def __init__(self,SYSTEM_TARGET_OBJECT,thread_id=0,timer_delay=0.0,random_byte_length=256):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        #self.daemon = True
        self.time_delay = timer_delay
        self.random_byte_length = random_byte_length
        self.System_Obj = SYSTEM_TARGET_OBJECT
        self.stay_alive = True
    
    def get_random_int(self,bytess):                                           # Change Random Function if required
        return Random.get_random_bytes(bytess)
    
    def generate_hash(self):
        self.x = self.get_random_int(self.random_byte_length)
        self.hash = hashlib.sha256(self.x).hexdigest()
        self.ret = int(self.hash,16)
        time.sleep(self.time_delay)
        return self.ret
    
    def run(self):
        global hashes_count,last_time
        while self.stay_alive == True:
            self.h = self.generate_hash()
            hashes_count +=1
            if(self.System_Obj.check_hash(self.h) == True):
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

for i in range(miner_count):
    x = Miner(a,i)
    x.start()

time.sleep(runtime)

for miner in miners:
    miner.halt_thread()

stop_time = time.time()

if(stop_time<start_time):
    stop_time +=60

time_elapsed = stop_time - start_time
hash_rate = (hashes_count/time_elapsed) / 1000

print("-"*60)
print("Total Miner-Threads     : {} ".format(miner_count))
print("Total Blocks Solved     : {} ".format(block_count))
print("Total Hashes Calculated : {} ".format(hashes_count))
print("Total Time Elapsed      : {} Seconds".format(stop_time-start_time))
print("HashRate for the Run    : {} KHashes/Sec".format(hash_rate))
print("-"*60)