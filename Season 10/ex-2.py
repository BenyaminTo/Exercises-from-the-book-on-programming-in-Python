import threading

# Shared variable
shared_resource = 0

# Create an RLock
rlock = threading.RLock()

# Create a Lock
lock = threading.Lock()

def increment_rlock():
    global shared_resource
    for _ in range(100000):
        with rlock:
            shared_resource += 1

def increment_lock():
    global shared_resource
    for _ in range(100000):
        with lock:
            shared_resource += 1

# Thread 1 for RLock
thread_rlock = threading.Thread(target=increment_rlock)
# Thread 2 for RLock
thread_rlock2 = threading.Thread(target=increment_rlock)

# Thread 1 for Lock
thread_lock = threading.Thread(target=increment_lock)
# Thread 2 for Lock
thread_lock2 = threading.Thread(target=increment_lock)

# Start the threads
thread_rlock.start()
thread_rlock2.start()
thread_lock.start()
thread_lock2.start()

# Wait for all threads to finish
thread_rlock.join()
thread_rlock2.join()
thread_lock.join()
thread_lock2.join()

print("Shared number with RLock:", shared_resource)
print("Shared number with Lock:", shared_resource)
