from multiprocessing import Process, Queue
import time


def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.put(total)
    return


if __name__ == '__main__':
    timestart = time.time()
    START, END = 0, 100000000
    result = Queue()
    th1 = Process(target=work, args=(1, START, END // 2, result))
    th2 = Process(target=work, args=(2, END // 2, END, result))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    result.put('STOP')
    total = 0
    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break
        else:
            print(tmp)
            total += tmp
    print(f"Result: {total}")
    timeend = time.time()
    print(f"Time: {timeend - timestart:.5f} sec")