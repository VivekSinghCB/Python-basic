# multiprocess with 'pipe' example

import multiprocessing

def sender(conn, msg):  # Function to send messages
    for i in msg:
        conn.send(i)  # Send each message via Pipe connection
    conn.close()  # Close connection after sending all messages

def receive(conn):  # Function to receive messages
    while True:
        try:
            msg = conn.recv()  # Receive message
        except Exception as e:
            print(e)
            break
        print(msg)

if __name__ == '__main__':  # Ensure correct execution in multiprocessing
    msg = ["My name is Vivek", "I am learning Python", "Wish me best learning"]
    parent_con, child_con = multiprocessing.Pipe()  # Create a pipe for inter-process communication

    m1 = multiprocessing.Process(target=sender, args=(child_con, msg))  # Create sender process
    m2 = multiprocessing.Process(target=receive, args=(parent_con,))  # Create receiver process

    m1.start()  # Start sender process
    m2.start()  # Start receiver process

    m1.join()  # Wait for sender to finish
    child_con.close()  # Close child connection
    m2.join()  # Wait for receiver to finish
    parent_con.close()  # Close parent connection
