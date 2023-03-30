"""
# 2개의 함수가 공통의 변수를 증가 / 감소 시키는 프록그램
# Lock을 통해서 순차적으로 처리

# Result : No lock : 
"""
import random
import threading
import time

count = 1
lock = threading.Lock()


def worker_A():
    global count, lock
    lock.acquire()
    while count < 10:
        count += 1
        print(f"worker A increase count : {count}")
        time.sleep(random.randint(0, 1))
    print("Finished work A")
    lock.release()


def worker_B():
    global count, lock
    lock.acquire()
    while count > -10:
        count -= 1
        print(f"worker B decrease count : {count}")
        time.sleep(random.randint(0, 1))
    print("Finished worker B")
    lock.release()


def main():
    t1 = time.time()
    thread_A = threading.Thread(target=worker_A)
    thread_B = threading.Thread(target=worker_B)

    thread_A.start()
    thread_B.start()

    thread_A.join()
    thread_B.join()

    print(f"Finished all process. Excution Time : {time.time() - t1}")


if __name__ == "__main__":
    main()
