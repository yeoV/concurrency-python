"""
# map() 함수를 이용하면 호출한 순서대로 반환, as_completed 완료한 순서대로 반환
"""
import time
import random
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed


values = [2, 3, 4, 5, 6]


def multiply_by_two(n):
    time.sleep(random.randint(1, 2))
    return 2 * n


def map_func():
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(multiply_by_two, values)

        for x in results:
            print(f"Done : {x}")


def completed_func():
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = []

        for value in values:
            task = executor.submit(multiply_by_two, (value))
            tasks.append(task)

        for result in as_completed(tasks):
            print(f"Task is completed : {result.result()}")


if __name__ == "__main__":
    map_func()
    completed_func()

### map function
# Done : 4
# Done : 6
# Done : 8
# Done : 10
# Done : 12
### as_completed
# Task is completed : 6
# Task is completed : 4
# Task is completed : 8
# Task is completed : 10
# Task is completed : 12
