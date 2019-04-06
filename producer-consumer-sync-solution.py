import time
import random
import threading

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

class Memory():
    def __init__(self):
        self.buffer_mutex = Semaphore(1)
        self.fill_count = Semaphore(0)
        self.empty_count = Semaphore(100)
        self.memory_buffer = []

class Consumer(threading.Thread):
    def __init__(self, memory, producer=None):
        super().__init__()
        self.memory = memory
        self.producer = producer
        self.sleep()
        
    def wake(self):
        self.awake = True
        self.asleep = False
    
    def sleep(self):
        self.awake = False
        self.asleep = True   
        
    def run(self):
        while True:            
            self.consume()
                
    def consume(self):
        self.memory.fill_count.down()
        self.memory.buffer_mutex.down()
        item = self.memory.memory_buffer.pop()
        print("Consumer consumes the item {}" .format(item))
        self.memory.buffer_mutex.up()
        self.memory.empty_count.up()
        

class Producer(threading.Thread):
    def __init__(self, memory, consumer=None):
        super().__init__()
        self.memory = memory
        self.consumer = consumer
        self.wake()
        
        
    def wake(self):
        self.awake = True
        self.asleep = False

    
    def sleep(self):
        self.awake = False
        self.asleep = True
        
    def run(self):
        while True:
            self.produce()
        
    def produce(self):
        it = random.randint(1, 10)
        print ("Producer produces {}" .format(it))
        self.memory.empty_count.down()
        self.memory.buffer_mutex.down()
        self.memory.memory_buffer.append(it)
        print ("Producer put {} in buffer memory" .format(it))
        self.memory.buffer_mutex.up()
        self.memory.fill_count.up()
        
        
def main():
    memory = Memory()
    consumer = Consumer(memory)
    producer = Producer(memory)
    consumer.producer = producer
    producer.consumer = consumer
    consumer.daemon = True
    producer.daemon = True
    consumer.start()
    producer.start()
    
    while True:
        if consumer.asleep and producer.asleep:
            print("Deadlock ocurred")
            break
    
    
    
if __name__ == "__main__":
    main()
