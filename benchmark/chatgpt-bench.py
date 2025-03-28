import time
import gc

# Benchmarking utility
def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {end - start:.6f} sec")
        return result
    return wrapper

# 1. Arithmetic operations
@benchmark
def arithmetic_test():
    x = 0
    for i in range(100000):  # Reduced range for MicroPython
        x += (i * 2) / (i + 1)
    return x

# 2. Recursion (Fibonacci)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@benchmark
def fibonacci_test():
    return fibonacci(20)  # Reduced n for MicroPython

# 3. Loop performance
@benchmark
def loop_test():
    s = 0
    for i in range(100000):  # Reduced range for MicroPython
        s += i
    return s

# 4. String operations
@benchmark
def string_test():
    s = "".join(str(i) for i in range(1000))  # Reduced range
    return "".join(reversed(s))  # Alternative to s[::-1]

# 5. List operations
@benchmark
def list_test():
    lst = list(range(1000))  # Reduced range
    lst.append(500)
    lst.sort()
    return lst[500]

# 6. Dictionary operations
@benchmark
def dict_test():
    d = {i: i * 2 for i in range(1000)}  # Reduced range
    return d[500]

# 7. File I/O
@benchmark
def file_io_test():
    with open("test_file.txt", "w") as f:
        for _ in range(1000):  # Reduced repetitions
            f.write("Hello, world!\n")
    with open("test_file.txt", "r") as f:
        return f.read()

# 8. Simple string search (replacing regex)
@benchmark
def string_search_test():
    text = "123 abc 456 def 789 ghi 101112"
    return [text[i:i+3] for i in range(len(text)-2) if text[i:i+3].isdigit()]

# 9. Garbage Collection
@benchmark
def gc_test():
    gc.collect()

# Run all benchmarks
if __name__ == "__main__":
    arithmetic_test()
    fibonacci_test()
    loop_test()
    string_test()
    list_test()
    dict_test()
    file_io_test()
    string_search_test()
    gc_test()

