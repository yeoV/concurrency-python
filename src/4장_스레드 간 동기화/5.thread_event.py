"""
# 파이썬 내장 함수에는 스레드를 완벽하게 종료하는 메커니즘이 없음.
# -> 이벤트 객체가 해제 상태일 때 스레드가 실행되게 할 수 있음.
# -> 프로그램 종료 및 스레드를 해제하기 전 대기하는 상황에서 유리
"""

import threading
import time


def my_thread(event):
    while not event.is_set():
        print("Waiting for Event to be set")
        time.sleep(1)
    print("Event has been set")


def main():
    event = threading.Event()
    thread1 = threading.Thread(target=my_thread, args=(event,))
    thread1.start()
    print("Thread is starting")
    time.sleep(10)
    event.set()

    thread1.join()
    print("Process is done")


if __name__ == "__main__":
    main()
