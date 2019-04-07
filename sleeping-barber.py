import time
import random
import threading

class Barber():
    def __init__(self):
        self.barberWorking = threading.Event()
        
    def sleep(self):
        print("Barber is sleeping")
        self.barberWorking.wait()
        
    def wake(self):
        self.barberWorking.set()
                
    def cut(self, costumer):        
        self.barberWorking.clear()
        print("Barber are cutting the hair from client {}".format(costumer.id))
        time.sleep(random.randint(1, 5))
        costumer.cut = True
        self.cutting = False
        print("Barber finished the hair cut")
            
class Barbershop():
    def __init__(self, free_chairs, barber):
        
        self.free_chairs = free_chairs         
        self.barber = barber
        self.waiting_room = []
        print("Barber shop is opening...")
        self.mutex = threading.Lock()
        working = threading.Thread(target=self.work)
        working.start()
    
    def work(self):
        while True:
            self.mutex.acquire()
            if len(self.waiting_room) > 0:
                client = self.waiting_room[0]                
                del self.waiting_room[0]
                self.mutex.release()
                self.barber.cut(client)
            else:
                self.mutex.release()
                print("Aaah, all done, going to sleep,,,")
                self.barber.sleep()
                print("Barber woke up")
            
        
    def receive_costumer(self, costumer):
        print("Client {} arrive" .format(costumer.id))
        self.mutex.acquire()
        if len(self.waiting_room) == self.free_chairs:
            print("Full wait room! Come back later")
            self.mutex.release()
            costumer.leave()
        else:
            self.waiting_room.append(costumer)
            costumer.sit = True
            print("Client {} is waiting in wait room" .format(costumer.id))
            self.mutex.release()
            self.barber.wake()
        
            
            
    def have_chair(self):
        for chair in self.waiting_room:
            if chair is None:
                return True
        return False

class Costumer(threading.Thread):
    def __init__(self, barbershop, id):
        super().__init__()
        self.id = id
        self.cut = False
        self.sit = False
        self.barbershop = barbershop
        
    def run(self):
        while not self.cut:
            if not self.sit:
                self.barbershop.receive_costumer(self)
            time.sleep(random.randint(1, 6))
        
    def leave(self):
        print("Costumer {} leaves the barbershop..." .format(self.id))

barber = Barber()
b = Barbershop(5, barber)            
clients = []
l = random.randint(10, 30)
for i in range(l):
    a = Costumer(b, i)
    clients.append(a)
    
for i in clients:
    time.sleep(random.randint(2, 5))
    i.start()
    
for i in clients:
    i.join()
