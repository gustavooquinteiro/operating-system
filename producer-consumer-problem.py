import time
import random
import threading

class Memory():
    def __init__(self):
        self.buffer_size = 100
        self.memory_buffer = []
        self.item_count = 0

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
        while True:
            if self.memory.item_count == 0:
                self.sleep()
                
            while not self.awake:
                time.sleep(random.randint(2, 5))
                
            item = self.memory.memory_buffer.pop()
            self.memory.item_count -= 1
            
            if self.memory.item_count == self.memory.buffer_size - 1:
                self.producer.wake()
            self.consume_item(item)
            
    def consume_item(self, item):
        print("Consumer consumes the item {}" .format(item))

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
        if self.memory.item_count == self.memory.buffer_size:
            self.sleep()
        
        while not self.awake:
            time.sleep(random.randint(2, 5))
            
        self.memory.memory_buffer.append(it)
        print ("Producer put {} in buffer memory" .format(it))
        self.memory.item_count += 1
        if self.memory.item_count == 1:
            self.consumer.wake()
        
            
    
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
        
if __name__ == "__main__" :
    main()
        
