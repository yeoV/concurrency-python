"""
문제:
파이썬에서는 스레드를 종료하는 내장 스레드 함수를 지원하지 않음
-> 자식 스레드 종료하지 않고 부모 스레도 종료 시, orpan thread

해결책:
프로세스에서 이러한 작업을 진행
"""
from multiprocessing import Process
import time


def my_worker():
    t1 = time.time()
    print(f"Process starting... at {t1}")
    time.sleep(10)


my_process = Process(target=my_worker)
print(f"Process info : {my_process}")
my_process.start()
print("Terminating Process")
my_process.terminate()
my_process.join()
print(f"Terminated Process. {my_process}")
