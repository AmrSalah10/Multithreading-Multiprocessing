import time
import concurrent.futures as futures

start = time.perf_counter()

def do_something(sec):
    print(f'Sleeping {sec} seconds')
    time.sleep(2)
    print(f'Woke up after {sec} seconds...')

# thread intialization
with futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    # return result when finished
    results = [executor.submit(do_something, sec) for sec in secs]
   
    # return result in FIFO 
    # map_results = executor.map(do_something, secs)

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} Seconds.") 


