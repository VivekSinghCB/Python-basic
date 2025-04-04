# Array example

import multiprocessing  # Import the multiprocessing module for parallel execution

# Function to square a specific element in the shared array
def square(index, value):  
    value[index] = value[index] ** 2  # Modify the shared array at the given index

# Main execution block (ensures safe execution in Windows)
if __name__ == '__main__':  
    # Create a shared array of integers with initial values
    arr = multiprocessing.Array('i', [8, 9, 3, 6, 4, 7, 2, 1])  
    
    process = []  # List to store process objects

    # Create and start 8 separate processes
    for i in range(8):  
        m = multiprocessing.Process(target=square, args=(i, arr))  # Create process
        process.append(m)  # Store process in the list
        m.start()  # Start the process

    # Ensure all processes finish execution
    for p in process:  
        p.join()  # Wait for the process to complete

    # Convert the shared array to a regular list and print the modified values
    print(list(arr))  