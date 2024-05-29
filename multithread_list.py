import threading
from threading import Thread
import time
import pickle

def work(start, end, step, result):
    total = 0
    for i in range(start, end, step):
        total += i
    result.append(total)
    return


if __name__ == '__main__':
    global_start_time = time.time()
    calc_time = list()
    x, y, z = list(), list(), list()

    for calc_amount in range(4, 33):
        for thread in range(1, 17):
            start_time = time.time()
            result = list()
            START, END = 0, 2 ** calc_amount

            workers = [Thread(target=work, args=(START + i, END, thread, result)) for i in range(thread)]
            for worker in workers: worker.start()

            for worker in workers: worker.join()

            end_time = time.time()

            total = sum(result)
            x.append(thread)
            y.append(calc_amount)
            z.append(end_time - start_time)
            print(f"{total} thread: {thread}, amount: {calc_amount}, time: {end_time - start_time}")

dic = {'thread': x, 'calc_amount': y, 'time': z}
with open('point.pkl', 'wb') as f:
    pickle.dump(dic, f)
print(time.time() - global_start_time)