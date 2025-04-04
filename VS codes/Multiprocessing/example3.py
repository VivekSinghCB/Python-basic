# multiprocess with 'producer' and 'consumer' example

import multiprocessing  # Importing the multiprocessing module

# Function to produce data and put it into the queue
def producer(q):  
    for i in range(10):  # Looping through numbers 0-9
        q.put(i)  # Putting each number into the queue

# Function to consume data from the queue
def consumer(q):  
    while True:  # Infinite loop to continuously get items from the queue
        item = q.get()  # Retrieving an item from the queue
        if item is None:  # If item is None, break the loop to stop the consumer
            break
        print(item)  # Print the item retrieved from the queue

if __name__ == '__main__':  # Ensuring that multiprocessing runs correctly
    queue = multiprocessing.Queue()  # Creating a queue for inter-process communication

    # Creating producer process
    m1 = multiprocessing.Process(target=producer, args=(queue,))  

    # Creating consumer process
    m2 = multiprocessing.Process(target=consumer, args=(queue,))  

    m1.start()  # Starting the producer process
    m2.start()  # Starting the consumer process

    m1.join()  # Wait for the producer process to complete
    m2.join()  # Wait for the consumer process to complete
