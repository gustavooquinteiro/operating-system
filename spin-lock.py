import time
import random
import threading
class Memory():
    def __init__(self, processes):
        self.turn = 0
        self.processes = processes        
        
    def calculate(self, process):
        return (process+1) % self.processes

    def critical_region(self, process):
        while self.turn != process.id:
            process.waiting = True
            print("Process {} is waiting to in critical region...".format(process.id))
            time.sleep(random.randint(1,5))
        process.waiting = False
        process.incriticalregion = True
        print("Process {} is in critical region...".format(process.id))
        time.sleep(random.randint(1, 5))
        

class Process(threading.Thread):
    def __init__(self, id, memory):
        super().__init__()
        self.id = id
        self.waiting = False
        self.memory = memory
        self.incriticalregion = True
        self.time = random.randint(1, 10)
        
    def run(self):
        while True:
            self.memory.critical_region(self)
            self.incriticalregion = False
            print("Process {} left critical region".format(self.id))
            time.sleep(self.time)
            self.memory.turn = self.memory.calculate(self.id)
  
def antecessor(number, n):
    if number == 0:
        return n - 1
    return number - 1

def main():
    n = random.randint(2, 5)
    memory = Memory(n)
    processes = []
    for i in range(n):
        p = Process(i, memory)
        print("Created Process {}..." .format(i))
        p.daemon = True
        processes.append(p)
    for i in processes:
        i.start()
    i = 0
    while True:
        predecessor = antecessor(i, n)
        if processes[i].waiting and not processes[predecessor].incriticalregion and processes[predecessor].time >= 3:    
            print("Busy wait problem ocurred:\n\t The actual process (Process {}) take too long to transfer to the next one (Process {})" .format(processes[predecessor].id, processes[i].id ))
            break
        i += 1
        if i > n-1:
            i = 0
            
if __name__ == "__main__":
    main()
        
