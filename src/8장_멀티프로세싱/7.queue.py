import multiprocessing as mp

VARS = [1, 2, 3]


def my_process(q: mp.Queue):
    val = q.get()
    print(f"Process PID : {mp.current_process().pid}, Value : {val}")
    q.task_done()  # 없을 경우, 계속 wait


def main():
    manager = mp.Manager()
    q = manager.Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    process1 = mp.Process(target=my_process, args=(q,))
    process1.start()
    process1.join()
    process2 = mp.Process(target=my_process, args=(q,))
    process2.start()
    process2.join()
    process3 = mp.Process(target=my_process, args=(q,))
    process3.start()
    process3.join()


if __name__ == "__main__":
    main()
