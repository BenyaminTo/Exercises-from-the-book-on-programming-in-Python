import threading
import pickle

# def insert_data_LOCK(UserN):
#     lock.acquire()
#     try:
#         with open("file", "ab") as file:
#             pickle.dump(UserN, file)
#             print("The user {} entered their data.".format(UserN))
#     finally:    
#         lock.release()
###############################################################################
# def insert_data_RLOCK(UserN):
#     rlock.acquire()
#     try:
#         with open("file", "ab") as file:
#             pickle.dump(UserN, file)
#             print("The user {} entered their data.".format(UserN))
#     finally:    
#         rlock.release()
###############################################################################
# def insert_data_SEMAPHORE(UserN):
#     semaphore.acquire()
#     try:
#         with open("file", "ab") as file:
#             pickle.dump(UserN, file)
#             print("The user {} entered their data.".format(UserN))
#     finally:    
#         semaphore.release()
###############################################################################
# def insert_data_EVENT(UserN):
#     try:
#         with open("file", "ab") as file:
#             pickle.dump(UserN, file)
#             print("The user {} entered their data.".format(UserN))
#     finally:    
#         event.set()
###############################################################################
def insert_data_EVENT(UserN):
    with condition:
        try:
             with open("file", "ab") as file:
                 pickle.dump(UserN, file)
                 print("The user {} entered their data.".format(UserN))
        finally:    
             condition.notify()
###############################################################################
def report_data():   
    with open("file", "rb") as file:
        file.seek(0, 0)
        ob = pickle.load(file)
        print(ob)

#Lock method
#lock = threading.Lock()
#thread1 = threading.Thread(target= insert_data_LOCK, args= (1,))
#thread2 = threading.Thread(target= insert_data_LOCK, args= (2,))

#thread1.start()
#thread2.start()

#thread1.join()
#thread2.join()

#report_data()

#RLock method
#rlock = threading.RLock()
#thread1 = threading.Thread(target= insert_data_RLOCK, args= (1,))
#thread2 = threading.Thread(target= insert_data_RLOCK, args= (2,))

#thread1.start()
#thread2.start()

#thread1.join()
#thread2.join()

#report_data()

#SEMAPHORE method
#semaphore = threading.Semaphore(1)
#threads = [threading.Thread(target=insert_data_SEMAPHORE, args= (i,)) for i in range(2)]

#for t in threads:
#    t.start()

#for t in threads:
#    t.join()

#report_data()

#EVENT method
# event = threading.Event()
# thread1 = threading.Thread(target= insert_data_EVENT, args= (1,))
# thread2 = threading.Thread(target= insert_data_EVENT, args= (2,))

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

#report_data()
#CONDITION method
condition = threading.Condition()
thread1 = threading.Thread(target= insert_data_EVENT, args= (1,))
thread2 = threading.Thread(target= insert_data_EVENT, args= (2,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

report_data()