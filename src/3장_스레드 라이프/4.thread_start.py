# Thread starting

import threading
import time
import random


def thread_run(idx):
    print(f"Start Thread num : {idx}")
    time.sleep(random.randint(0, 10))
    print(f"Finish Thread execution : {idx}")


# 한번에 스레드 모두 실행
for idx in range(10):
    thread = threading.Thread(target=thread_run, args=(idx,))
    thread.start()

    print(f"Active Thread : {threading.enumerate()}")
