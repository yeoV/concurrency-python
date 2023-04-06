from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import threading

values = [2, 3, 4, 5, 6, 7, 8]


def multiply_by_two(n: int):
    return 2 * n


def main():
    global values
    with ThreadPoolExecutor(max_workers=3) as excutor:
        results = excutor.map(multiply_by_two, values)
    print(*results)


if __name__ == "__main__":
    main()
