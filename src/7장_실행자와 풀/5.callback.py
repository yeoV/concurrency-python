"""
# Callback func
"""

from concurrent.futures import ThreadPoolExecutor


def task(n):
    print(f"Processing {n}")


def task_done(fn):
    if fn.done():
        print("Task is completed")
    elif fn.cancelled():
        print(f"Our {fn} Future has been cancelled")


def second_task(fn):
    print("Executing Second Task")


def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        future = executor.submit(task, (1))
        future.add_done_callback(task_done)
        future.add_done_callback(second_task)


if __name__ == "__main__":
    main()
