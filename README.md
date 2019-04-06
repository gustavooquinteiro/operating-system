# Operational-system
Implementing known synchronization problems in Python 

## Dining philosophers problem

Here is an adaptation of [Wikipedia's description](https://en.wikipedia.org/wiki/Dining_philosophers_problem): 
    

> Five silent philosophers sit at a round table with bowls of spaghetti. Hashis are placed between each pair of adjacent philosophers.
> 
> Each philosopher must alternately think and eat. However, a philosopher can only eat spaghetti when they have both left and right hashis. Each hashi can be held by only one philosopher and so a philosopher can use the hashi only if it is not being used by another philosopher. After an individual philosopher finishes eating, they need to put down both hashis so that the hashis become available to others. A philosopher can take the hashi on their right or the one on their left as they become available, but cannot start eating before getting both hashis.
> 
> Eating is not limited by the remaining amounts of spaghetti or stomach space; an **infinite supply** and an **infinite demand** are assumed.
> 
> The problem is how to design a discipline of behavior (a concurrent algorithm) such that no philosopher will starve; i.e., each can forever continue to alternate between eating and thinking, assuming that no philosopher can know when others may want to eat or think. 
> 

The [first approach](philosofer-dinner-first-approach.py) uses a naive solution where the philosopher waits until the hashi that he need is free to use.

- This solution brings the [deadlock problem](https://en.wikipedia.org/wiki/Deadlock) when all philosophers holds one hashi and waits the other to eat. 

- The program can detect the deadlock when happens.

The [second approach](philosofer-dinner-second-approach.py) to try prevent the deadlock makes the philosopher, when he don't get the second hashi, put back the first that he got.

- This solution brings the [starvation problem](https://en.wikipedia.org/wiki/Starvation_(computer_science\)) when all philosophers pick up the first hashi and put it back when they didn't get the second hashi.

- The program was supposed to detect the starvation when happens. Working on it
