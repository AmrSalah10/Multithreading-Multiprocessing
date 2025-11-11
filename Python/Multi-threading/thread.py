import time
import threading

start = time.perf_counter()

def do_something(thread):
    print(f'{thread} Sleeping 2 seconds')
    time.sleep(2)
    print(f'{thread} Woke up...')

# thread intialization
t1= threading.Thread(target=do_something, args=('t1',))
t2 = threading.Thread(target=do_something, args=('t2',))

# start threads
t1.start()
t2.start()

# wait threads to finish
t1.join()
t2.join()


finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} Seconds.") 


# Total time -> 
#    sync: 4 sec
#    concurrently (threads): 2 sec

