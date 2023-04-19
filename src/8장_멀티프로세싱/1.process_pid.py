"""
# 모든 프로세스는 pid를 가지고 있다.
"""

import multiprocessing
import time


def child_task():
    print(f"Child Process with PID : {multiprocessing.current_process().pid}")
    time.sleep(3)
    print(f"Child process terminating")


def main():
    print(f"Main Process PID : {multiprocessing.current_process().pid}")
    my_process = multiprocessing.Process(target=child_task())
    my_process.start()
    my_process.join()


if __name__ == "__main__":
    main()
