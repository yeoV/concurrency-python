import multiprocessing
import os


class MyProcess(multiprocessing.Process):
    def __init__(self):
        super(MyProcess, self).__init__()

    def run(self):
        print(f"Child Process PID : {multiprocessing.current_process().pid}")


def main():
    print("----------------Single Child Process---------------")
    print(f"Main Process PID : {multiprocessing.current_process().pid}")
    my_process = MyProcess()
    my_process.start()
    # my_process.run()
    my_process.join()
    print("----------------CPU Core's Child Process---------------")
    processes = []
    for _ in range(os.cpu_count()):
        process = MyProcess()
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    main()
