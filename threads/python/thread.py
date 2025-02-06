import threading
import os
import time

def task(name, delay):
    for i in range(100):
        print(f"Child: Task {name}, Iteration {i}, PID {os.getpid()} Thread ID {threading.get_ident()}")
        time.sleep(delay)

def main():
    print(f"Parent: {os.getpid()}")

    # concurrent threads
    thread1 = threading.Thread(target= task, args=("A", 1))
    thread2 = threading.Thread(target= task, args=("A", 2))

    thread1.start()
    thread2.start()

    # join threads to main thread
    thread1.join()
    thread2.join()

    time.sleep(100)

    print("Oh Wait it doesnt work like that")
main()
