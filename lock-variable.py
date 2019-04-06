import time
import random
import threading
class Memory():
    def __init__(self):
        self.lock = False
        self.count = 0
        
    def critical_region(self, id):
        while self.lock is True:
            print("Process {} is waiting to in critical region...".format(id))
            time.sleep(random.randint(1,5))
        self.lock = True
        self.count += 1
        print("Process {} is in critical region...".format(id))
        if self.count == 2:
            print("2 processes in critical region")
            raise Exception()
        time.sleep(random.randint(1, 5))
        self.lock = False
        self.count -= 1
        print("Process {} left critical region".format(id))
        

class Process(threading.Thread):
    def __init__(self, id, memory):
        super().__init__()
        self.id = id
        self.memory = memory
        
    def run(self):
        while True:
            try:
                self.memory.critical_region(self.id)
                time.sleep(random.randint(1, 5))
            except e as Exception:
                raise Exception()
            
    
        
   
def main():
    memory = Memory()
    n = random.randint(2, 5)
    processes = []
    for i in range(n):
        p = Process(i, memory)
        print("Created Process {}..." .format(i))
        p.daemon = True
        p.start()
        processes.append(p)
        
    for p in processes:
        p.join()
if __name__ == "__main__":
    main()
        
