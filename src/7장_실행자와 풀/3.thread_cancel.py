import time
import random
from concurrent.futures import ThreadPoolExecutor


def some_task(n):
    print(f"Executing task {n}")
    time.sleep(n)
    print(f"Task {n} Finished Executing")


def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        task1 = executor.submit(some_task, (1))
        task2 = executor.submit(some_task, (2))
        task3 = executor.submit(some_task, (3))
        task4 = executor.submit(some_task, (4))

        print(task3.cancel())  # thread cancel 시, True 반환


if __name__ == "__main__":
    main()
