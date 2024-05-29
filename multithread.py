from threading import Thread
import time


def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.append(total)
    return


if __name__ == '__main__':
    timestart = time.time()
    START, END = 0, 100000000
    result = list()

    if not True:
        th1 = Thread(target=work, args=(1, START, END // 6, result))
        th2 = Thread(target=work, args=(2, END // 6, END // 6 * 2, result))
        th3 = Thread(target=work, args=(3, END // 6 * 2, END // 6 * 3, result))
        th4 = Thread(target=work, args=(4, END // 6 * 3, END // 6 * 4, result))
        th5 = Thread(target=work, args=(5, END // 6 * 4, END // 6 * 5, result))
        th6 = Thread(target=work, args=(6, END // 6 * 5, END, result))

        th1.start()
        th2.start()
        th3.start()
        th4.start()
        th5.start()
        th6.start()
        th1.join()
        th2.join()
        th3.join()
        th4.join()
        th5.join()
        th6.join()
    else:
        th = Thread(target=work, args=(1, START, END, result))

        th.start()
        th.join()

    print(result)
    print(f"result: {sum(result)}")
    timeend = time.time()
    print(f"time: {timeend - timestart:.5f} sec")
