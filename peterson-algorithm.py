import time 
import random
import threading

class Memory():
    def __init__(self, processes):
        self.quantity = processes
        self.flag = [False] * processes
        self.turn = 0
        
    def calculate_next_process(self, process):
        return (process+1) % self.quantity
    
    def enter_region(self, thread):
        other = self.calculate_next_process(thread)
        self.flag[thread] = True
        turn = thread
        while self.turn == thread and self.flag[other]:
            time.sleep(random.randint(1, 3))
        
    def leave_region(self, thread):
        self.flag[thread] = False
        
            
class Process(threading.Thread):
    def __init__(self, id, memory):
        super().__init__()
        self.id = id
        self.memory = memory
        self.incriticarea = False
        
    def run(self):
        while True:
            while self.memory.turn != self.id:
                time.sleep(random.randint(1, 3))
            
            self.memory.enter_region(self.id)
            self.incriticarea = True
            print("Process {} is in the critic area" .format(self.id))
            time.sleep(random.randint(1, 5))
            
            self.memory.leave_region(self.id)
            self.incriticarea = False
            print("Process {} left the critic area" .format(self.id))
            
            self.memory.turn = self.memory.calculate_next_process(self.id)
            time.sleep(1)
            
def main():
    n = int(input("Type the quantity of processes: "))
    memory = Memory(n)
    processes = []
    for i in range(n):
        p = Process(i, memory)
        p.daemon = True
        print("Create Process {}" .format(i))
        p.start()
        processes.append(p)
        
    for p in processes:
        p.join()
            
if __name__ == "__main__":
    main()
