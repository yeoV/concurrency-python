import threading
import time
import random


def my_thread(idx):
    print(f"Thread {idx}:  started")
    time.sleep(random.randint(1, 5))
    print(f"Thread {idx} : finished")


def main():
    for idx in range(random.randint(1, 10)):
        thread = threading.Thread(target=my_thread, args=(idx,))
        thread.start()
    time.sleep(4)
    print(f" Activate Thread : {threading.active_count()}")
    print("Finished ")


if __name__ == "__main__":
    main()
