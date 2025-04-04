# multiprocess with 'pool' example

import multiprocessing  # Importing the multiprocessing module to utilize multiple CPU cores

def square(n):  # Defining a function that takes an integer 'n' and returns its square
    return n**2

if __name__ == '__main__':  # Ensuring that the multiprocessing code runs only in the main script
    with multiprocessing.Pool(processes=4) as pool:  # Creating a pool of 4 worker processes
        m = pool.map(square, [5,9,6,3,7,5,4,2,7])  # Distributes elements of the list to worker processes for parallel execution
        print(m)  # Prints the list of squared values once all processes complete
