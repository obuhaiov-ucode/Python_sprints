import threading
import time

def task_thread(name, path, delay):
    with open(path, 'r') as f:
        for line in f:
            print(f"[{name}]: {line[:-1]}")
            time.sleep(delay)

def start_threads(jobs):
    for task in jobs:
        t = threading.Thread(target=task_thread, args=(task['name'], task['path'], task['delay']))
        t.start()
