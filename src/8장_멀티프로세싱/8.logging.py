import logging
import sys
import multiprocessing

logging.basicConfig(
    level=logging.INFO,
    format="%(processName)-10s %(asctime)s:%(levelname)s:%(message)s",
    handlers=[logging.FileHandler("myapp.log"), logging.StreamHandler(sys.stdout)],
)


def my_task(n):
    logging.info(f"Processed Result : {n * 2}")
    return n * 2


def main():
    with multiprocessing.Pool(4) as p:
        p.map(my_task, [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    main()


# SpawnPoolWorker-1 2023-04-14 09:40:53,569:INFO:Processed Result : 2
# SpawnPoolWorker-2 2023-04-14 09:40:53,569:INFO:Processed Result : 4
# SpawnPoolWorker-1 2023-04-14 09:40:53,569:INFO:Processed Result : 6
# SpawnPoolWorker-2 2023-04-14 09:40:53,569:INFO:Processed Result : 8
# SpawnPoolWorker-1 2023-04-14 09:40:53,570:INFO:Processed Result : 10
# SpawnPoolWorker-2 2023-04-14 09:40:53,570:INFO:Processed Result : 12
