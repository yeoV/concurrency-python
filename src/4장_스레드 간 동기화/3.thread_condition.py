"""
# primitive Lock 3. Condition
- 다른 스레드의 신호를 기다리는 primitive
- Pub / Sub 구조로 특정 스레드의 종료 알림을 받는 순간 Lock 획득 / 해제
"""
from typing import List

import threading
import time
import random


class publisher(threading.Thread):
    condition: threading.Condition
    integers: List

    def __init__(self, condition, integers):
        self.condition = condition
        self.integers = integers
        threading.Thread.__init__(self)

    def run(self):
        for _ in range(2):
            integer = random.randint(0, 100)
            self.condition.acquire()
            print(f"Acquired condition : {self.name}")
            self.integers.append(integer)
            print(f"Appending Integer : {integer}")
            self.condition.notify()
            self.condition.release()
            print("Released Condition")
            time.sleep(4)


class subscriber(threading.Thread):
    condition: threading.Condition
    integers: List

    def __init__(self, condition, integers):
        self.condition = condition
        self.integers = integers
        threading.Thread.__init__(self)

    def run(self):
        self.condition.acquire()
        print(f"Acquired Condition : {self.name}")
        while True:
            if self.integers:
                integer = self.integers.pop()
                print(f"{integer} Popped from List")
                break
            print(f"{self.name} Wait Publishing...")
            self.condition.wait()
        print(f"Released Condition : {self.name}")
        self.condition.release()


def main():
    integers = list()
    condition = threading.Condition()

    pub1 = publisher(condition, integers)
    pub1.start()

    sub1 = subscriber(condition, integers)
    sub2 = subscriber(condition, integers)
    sub1.start()
    sub2.start()

    pub1.join()
    sub1.join()
    sub2.join()

    print(f"Finished Condition Lock Process")


if __name__ == "__main__":
    main()
