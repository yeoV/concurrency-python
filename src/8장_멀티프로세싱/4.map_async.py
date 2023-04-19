from multiprocessing import Pool
import time
from timeit import default_timer


def my_task(n):
    time.sleep(n / 2)
    return n * 2


def main():
    print("Mapping array to Pool")
    t1 = default_timer()
    with Pool(4) as p:
        print(p.map(my_task, [4, 3, 2, 1]))
    print(f"Processed Time : {default_timer() - t1}")

    print("Mapping async array to Pool")
    t2 = default_timer()
    with Pool(4) as p:
        print(p.map_async(my_task, [8, 7, 6, 5]).get())
    print(f"Processed Time : {default_timer() - t2}")


if __name__ == "__main__":
    main()
