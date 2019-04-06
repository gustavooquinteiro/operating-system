"""
    A first Philosofer's Dinner approach where deadlocks happens
"""

import time 
import random
import threading

hashis = [False] * 5       
philosofers =["A", "B", "C", "D", "E"]        

class Philosofer(threading.Thread):
    def __init__(self, id):
        """Initiates the philosofer' properties """
        super().__init__()
        self.id = philosofers[id]
        self.left = id
        self.right = (id + 1) % len(hashis)
        self.n_hashis = 0
        self.waiting = False
        self.eating = False
        self.thinking = True
        
    def run(self):
        """The cerne of a philosofer: think and eat """
        while True:
            self.think()
            self.eat()
            
    def think(self):
        """ Think a certain amount of time """
        self.thinking = True
        print("Philosofer {} is thinking..." .format(self.id))
        time.sleep(random.randint(1, 5))
        
    def eat(self):
        """ Eat the pasta when get the hashis """
        self.take_hashi(self.left)
        self.take_hashi(self.right)
        self.thinking = False
        self.eating = True
        print("Philosofer {} is eating..." .format(self.id))
        time.sleep(random.randint(1, 10))
        self.eating = False
        self.return_hashi(self.left)
        self.return_hashi(self.right)
        print("Philosofer {} over your meal" .format(self.id))
    
        
    def take_hashi(self, i):
        """ Try to get the hashi nearby """
        if self.n_hashis >= 0 or self.n_hashis < 2:
            self.waiting = True
            while hashis[i]:
                print("Philosofer {} waiting the hashi {}" .format(self.id, i))
                time.sleep(random.randint(1, 5))
            self.waiting = False
            self.n_hashis += 1
            hashis[i] = True
            print("Philosofer {} took the hashi {}" .format(self.id, i))
        
        
    def return_hashi(self, i):
        """ Return the hashi to the table """
        hashis[i] = False
        self.n_hashis -= 1
        print("Philosofer {} returned the hashi {}" .format(self.id, i))

def main():
    print("Philosofer's dinner is starting")        
    filosofos =[]
    for i in range(5):
        print("Philosofer {} arrive" .format(philosofers[i]))
        a = Philosofer(i)
        a.start()
        filosofos.append(a)

    while True:
        # If all hashis are taken by the philosofers and all the philosofers are waiting other hashi 
        if all(hashis) and all(i.waiting for i in filosofos):
            print("Deadlock ocurred")
            break        
    print("Philosofer's dinner is over")

main()
