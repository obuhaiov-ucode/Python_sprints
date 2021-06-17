from multiprocessing import Process
import datetime
import time

def task_process(name, year, delay):
    y = datetime.datetime.now().year
    print(f"{name}, {y - year} years old")
    time.sleep(delay)

def start_processes(jobs):
    for task in jobs:
        p = Process(target=task_process, args=(task['name'], task['year'], task['delay']))
        p.start()
