"""
    A second Philosofer's Dinner approach where starvations happens
"""

import time 
import random
import threading 

hashis = [False] * 5       
hungry = [False] * 5
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
            self.take_hashis()
            self.eat()
            self.return_hashis()
            
    def think(self):
        """ Think a certain amount of time """
        self.thinking = True
        print("Philosofer {} is thinking..." .format(self.id))
        time.sleep(random.randint(1, 5))
        
    def eat(self):
        """ Eat the pasta when get the hashis """
        self.thinking = False
        self.eating = True
        print("Philosofer {} is eating..." .format(self.id))
        time.sleep(random.randint(1, 10))
        self.eating = False
        print("Philosofer {} over your meal" .format(self.id))
    
        
    def take_hashis(self):
        """ Try to get the hashi nearby """
        self.thinking = False
        count = 0
        hungryness = random.randint(10, 200)
        while self.n_hashis != 2:            
            count += 1
            if self.n_hashis == 0:
                if not hashis[self.left]:
                    hashis[self.left] = True
                    self.n_hashis += 1
                    print("Philosofer {} took the hashi {}" .format(self.id, self.left))
            if self.n_hashis == 1:
                if hashis[self.right]:
                    hashis[self.left] = False
                    self.n_hashis -= 1
                    print("Philosofer {} returned the hashi {}" .format(self.id, self.left))
                    self.waiting = True
                    time.sleep(random.randint(1, 5))
                else:
                    hungry[self.left] = False
                    self.waiting = False
                    hashis[self.right] = True
                    self.n_hashis += 1
                    print("Philosofer {} took the hashi {}" .format(self.id, self.right))
                if count > hungryness:
                    hungry[self.left] = True
                    print("Philosofer {} is hungry" .format(self.id))   
        
    def return_hashis(self):
        """ Return the hashi to the table """
        hashis[self.left] = False
        print("Philosofer {} returned the hashi {}" .format(self.id, self.left))
        hashis[self.right] = False
        print("Philosofer {} returned the hashi {}" .format(self.id, self.right))
        self.n_hashis = 0

def main():
    print("Philosofer's dinner is starting")        
    filosofos =[]
    for i in range(5):
        print("Philosofer {} arrive" .format(philosofers[i]))
        a = Philosofer(i)
        a.setDaemon(True)
        a.start()
        filosofos.append(a)

    while True:
        # If any philosofer is hungry and can't eat
        if any(hungry) or any(i.waiting for i in filosofos):
            print("Starvation ocurred")
            break        
    print("Philosofer's dinner is over")

main()
