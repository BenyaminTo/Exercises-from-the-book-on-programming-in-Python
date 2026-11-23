import threading
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def get_current_count(self):
        return self.count

counter = Counter()
print("Start: ",counter.get_current_count())
tr_1 = threading.Thread(target = counter.increment, name= 'tr_1')
tr_2 = threading.Thread(target = counter.increment, name= 'tr_2')
tr_3 = threading.Thread(target = counter.increment, name= 'tr_3')

tr_1.start()
print("Thread 1:",counter.get_current_count())
tr_2.start()
print("Thread 2:",counter.get_current_count())
tr_3.start()
print("Thread 3:",counter.get_current_count())

tr_1.join()
tr_2.join()
tr_3.join()
