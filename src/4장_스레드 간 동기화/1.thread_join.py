"""
.join() 메소드는 Child Thread가 확실하게 끝날때 까지를 보장해준다.
"""

import threading
import time


def our_thread(idx):
    print(f"Thread {idx} started")
    time.sleep(idx * 2)
    print(f"Thread {idx} finished")


def main():
    thread1 = threading.Thread(target=our_thread, args=(1,))
    thread1.start()
    print(f"Is thread1 is finished??")
    thread2 = threading.Thread(target=our_thread, args=(2,))
    thread2.start()
    thread2.join()
    print(f"Thread2 is definitely finished ")


if __name__ == "__main__":
    main()
