import time

def memory_write_test(num_writes):
    data = []
    start_time = time.time()
    for i in range(num_writes):
        data.append(i)
    print(f"Time: {time.time() - start_time:.6f} seconds")

memory_write_test(1000000)

