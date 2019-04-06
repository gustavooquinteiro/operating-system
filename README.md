# Operating systems
Implementing known synchronization problems in Python as a way to study the interprocess communication (IPC), race conditions and mutual exclusion in critical region. 

Subjects seen in Operating Systems - MATA58, taught by the Maycon Leone Maciel Peixoto in Federal University of Bahia (UFBA) 
    

## Dining philosophers problem

Here is an adaptation of [Wikipedia's description](https://en.wikipedia.org/wiki/Dining_philosophers_problem): 
    

> Five silent philosophers sit at a round table with bowls of spaghetti. Hashis are placed between each pair of adjacent philosophers.
> 
> Each philosopher must alternately think and eat. However, a philosopher can only eat spaghetti when they have both left and right hashis. Each hashi can be held by only one philosopher and so a philosopher can use the hashi only if it is not being used by another philosopher. After an individual philosopher finishes eating, they need to put down both hashis so that the hashis become available to others. A philosopher can take the hashi on their right or the one on their left as they become available, but cannot start eating before getting both hashis.
> 
> Eating is not limited by the remaining amounts of spaghetti or stomach space; an **infinite supply** and an **infinite demand** are assumed.
> 
> The problem is how to design a discipline of behavior (a concurrent algorithm) such that no philosopher will starve; i.e., each can forever continue to alternate between eating and thinking, assuming that no philosopher can know when others may want to eat or think. 


The [first approach](philosofer-dinner-first-approach.py) uses a naive solution where the philosopher waits until the hashi that he need is free to use.

- This solution brings the [deadlock problem](https://en.wikipedia.org/wiki/Deadlock) when all philosophers holds one hashi and waits the other to eat. 

- The program can detect the deadlock when happens.

The [second approach](philosofer-dinner-second-approach.py) to try prevent the deadlock makes the philosopher, when he don't get the second hashi, put back the first that he got.

- This solution brings the [starvation problem](https://en.wikipedia.org/wiki/Starvation_(computer_science)) when all philosophers pick up the first hashi and put it back when they didn't get the second hashi.

- The program can detect the starvation when happens.

The [solution](philosofer-dinner-sync-solution.py) is use a mutex semaphore to indicates to all the philosopher when the hashi is available or not, making the philosopher waits safely until he get the hashis. 

## Producer–consumer problem

Here is a description from [Wikipedia](https://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem):

> In computing, the producer–consumer problem (also known as the bounded-buffer problem) is a classic example of a multi-process synchronization problem. The problem describes two processes, the producer and the consumer, who share a common, fixed-size buffer used as a queue. The producer's job is to generate data, put it into the buffer, and start again. At the same time, the consumer is consuming the data (i.e., removing it from the buffer), one piece at a time. The problem is to make sure that the producer won't try to add data into the buffer if it's full and that the consumer won't try to remove data from an empty buffer.
>
> The solution for the producer is to either go to sleep or discard data if the buffer is full. The next time the consumer removes an item from the buffer, it notifies the producer, who starts to fill the buffer again. In the same way, the consumer can go to sleep if it finds the buffer empty. The next time the producer puts data into the buffer, it wakes up the sleeping consumer.
> The problem can also be generalized to have multiple producers and consumers. 

This [algorithm](producer-consumer-problem.py) uses a naive approach described in the problem' definition: if there are a item in buffer wakes a consumer if don't put him to sleep and wakes the producer. If the buffer is full put the producer to sleep and wakes the consumer.

- This implementation can lead to a deadlock in this [described scenario](https://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem#Inadequate_implementation)

- The program can detect the deadlock when happens.

This is the [solution](producer-consumer-sync-solution.py) using mutexes semaphores to control the buffer emptyness and fullness, and didn't put anyone (producer or consumer) to sleep indefinitively.

## Peterson algorithm

[Full description here](https://en.wikipedia.org/wiki/Peterson%27s_algorithm#The_algorithm)

> Peterson's algorithm (or Peterson's solution) is a concurrent programming algorithm for mutual exclusion that allows two or more processes to share a single-use resource without conflict, using only shared memory for communication. It was formulated by Gary L. Peterson in 1981.
>
> While Peterson's original formulation worked with only two processes, the algorithm can be generalized for more than two.

The generalized algorithm for 2 or more processes are implemented [here](peterson-algorithm.py)

## [Lock variable](lock-variable.py)

> A lock variable provides the simplest synchronization mechanism for processes. Some noteworthy points regarding Lock Variables are:
>
>   1. Its a software mechanism implemented in user mode, i.e. no support required from the Operating System.
>
>   2. Its a [busy waiting](https://en.wikipedia.org/wiki/Busy_waiting) solution (keeps the CPU busy even when its technically waiting).
>
>   3. It can be used for more than two processes.
> 
> When Lock = 0 implies critical section is vacant (initial value ) and Lock = 1 implies critical section occupied.

## [Spin Lock](spin-lock.py)

Full description [here](https://en.wikipedia.org/wiki/Spinlock)
