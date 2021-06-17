import time
from multiprocessing import Process, Queue
from queue import Empty


# leave class Ball as is, don't edit it
class Ball:
    def __init__(self, name, n_bounces):
        self.name = name
        self.n_bounces = n_bounces

    def __str__(self):
        return f'{self.name} ({self.n_bounces})'


# edit the function as described in comments
def bounce(name, delay, task_queue, done_queue):
    while True:
        time.sleep(delay)
        # write you code here
        # required actions:
        # - stop if done_queue is full
        if done_queue.full():
            print(f"[{name}] done_queue is full. Process will stop.")
            break
        try:
            new_ball = task_queue.get(1, 1)
            new_ball.n_bounces -= 1
            if new_ball.n_bounces == 0:
                done_queue.put(new_ball)
            else:
                task_queue.put(new_ball)
            pass  # replace with your code
            # required actions:
            # - get a ball from task_queue (wait for it max 1 second)
        except Empty:
            print(f'queue.Empty exception.')
        else:
            pass  # replace with your code
            # required actions:
            # - update the ball's counter
            # - put ball either back to the task_queue, or to the done_queue
        print(f'{name} bounces the {new_ball.name} ({new_ball.n_bounces}).')  # edit contents of the message


# edit the contents of this function in the allowed section
def run_processes(balls, args):
    processes = []
    task_queue = Queue()
    done_queue = Queue(len(balls))  # edit to make done_queue limited to the correct size

    # write your code here
    # required actions:
    # - create and start processes for each item of args
    # - put all the balls into the task_queue

    for ball in balls:
        task_queue.put(ball)
    for name, delay in args:
        new_proc = Process(target=bounce, args=(name, delay, task_queue, done_queue))
        new_proc.start()
        processes.append(new_proc)
    for p in processes:
        p.join()
