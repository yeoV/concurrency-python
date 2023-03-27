# Process forking, exec 과정
import os


def child():
    print(f"We are in child process PID : {os.getpid()}")


def parent():
    print(f"We are in parent process PID : {os.getpid()}")

    new_ref = os.fork()
    # time.sleep(2)
    print(f"new_pid : {new_ref}")

    if new_ref == 0:
        child()
    else:
        print(f"Already has child pid : {new_ref}")


if __name__ == "__main__":
    parent()
