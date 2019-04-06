"""
    A final Philosofer's Dinner approach where starvation and deadlocks doesnt happens
"""

import time 
import random
import threading 

hungry = []
philosofers =["A", "B", "C", "D", "E"]        

class Semaphore():
    def __init__(self, initial = 0):
        self.lock = threading.Condition(threading.Lock())
        self.value = initial
        
    def up(self):
        with self.lock:
            self.value += 1
            self.lock.notify()
            
    def down(self):
        with self.lock:
            while self.value == 0:
                self.lock.wait()
            self.value -= 1
        
class Hashi():
    def __init__(self, id):
        self.id = id
        self.lock = threading.Condition(threading.Lock())
        self.taken = False
        
    def take(self, id):
        with self.lock:
            while self.taken:
                self.lock.wait()
            self.taken = True
            print("Philosofer {} took the hashi {}" .format(id, self.id))
            self.lock.notifyAll()
            
            
    def drop(self, id):
        with self.lock:
            while not self.taken:
                self.lock.wait()
            self.taken = False
            print("Philosofer {} returned the hashi {}" .format(id, self.id))
            self.lock.notifyAll()


            
class Philosofer(threading.Thread):
    def __init__(self, id, left, right, semaphore):
        """Initiates the philosofer' properties """
        super().__init__()
        self.id = philosofers[id]
        self.left = left
        self.right = right
        self.semaphore = semaphore
        
    def run(self):
        """The cerne of a philosofer: think and eat """
        while True:
            self.think()
            self.semaphore.down()
            self.left.take(self.id)
            self.right.take(self.id)
            self.eat()
            self.left.drop(self.id)
            self.right.drop(self.id)
            self.semaphore.up()
            
    def think(self):
        """ Think a certain amount of time """
        print("Philosofer {} is thinking..." .format(self.id))
        time.sleep(random.randint(1, 5))
        
    def eat(self):
        """ Eat the pasta when get the hashis """
        print("Philosofer {} is eating..." .format(self.id))
        time.sleep(random.randint(1, 10))
        print("Philosofer {} over your meal" .format(self.id))
    

def main():
    print("Philosofer's dinner is starting")        
    n = 5
    semaphore = Semaphore(n-1)
    hashis = [Hashi(i) for i in range(n)]
    filosofos = []
    for i in range(5):
        print("Philosofer {} arrive" .format(philosofers[i]))
        a = Philosofer(i, hashis[i], hashis[(i+1)%n], semaphore)
        a.start()
        filosofos.append(a)

    for philosofer in filosofos:
        philosofer.join()
        
    print("Philosofer's dinner is over")

if __name__ == "__main__":
    main()
