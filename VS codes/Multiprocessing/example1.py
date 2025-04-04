# Multiprocessing- allows the execution of multiple processes simultaneously, taking advantage of multi-core CPUs to achieve true parallel execution
 # Uses multiple processes, each with its own memory, Separate memory (more overhead but safer execution), A process crash is isolated and won’t affect others


# multiprocess with 'process' example
# Importing the multiprocessing module to create and manage multiple processes
import multiprocessing  

# Defining a function that will run as a separate process
def test1():  
    print("This is my multiprocessing program")  # Printing a message from the child process

# Ensuring that the script runs only when executed directly (not when imported as a module)
if __name__ == '__main__':  
    
    # Creating a new process that will run the function test1
    m = multiprocessing.Process(target=test1)  
    
    # Printing a message from the main program before starting the child process
    print("This is main program")  
    
    # Starting the child process (it runs test1 function in a separate execution space)
    m.start()  
    
    # Waiting for the child process to complete execution before continuing
    m.join()  
